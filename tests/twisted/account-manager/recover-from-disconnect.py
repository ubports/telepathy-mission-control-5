# Copyright (C) 2009 Nokia Corporation
# Copyright (C) 2009-2010 Collabora Ltd.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301 USA

import dbus
import dbus
import dbus.service

from servicetest import (EventPattern, tp_name_prefix, tp_path_prefix,
        call_async, sync_dbus, assertEquals)
from mctest import exec_test, SimulatedConnection, create_fakecm_account,\
        SimulatedChannel
import constants as cs

def test(q, bus, mc):
    cm_name_ref = dbus.service.BusName(
            tp_name_prefix + '.ConnectionManager.fakecm', bus=bus)

    # Create an account. We're setting register=True here to verify
    # that after one successful connection, it'll be removed (fd.o #28118).
    params = dbus.Dictionary({"account": "someguy@example.com",
        "password": "secrecy",
        "register": True}, signature='sv')
    (cm_name_ref, account) = create_fakecm_account(q, bus, mc, params)

    account_iface = dbus.Interface(account, cs.ACCOUNT)
    account_props = dbus.Interface(account, cs.PROPERTIES_IFACE)

    call_async(q, account, 'Set', cs.ACCOUNT, 'Enabled', False,
            dbus_interface=cs.PROPERTIES_IFACE)
    q.expect('dbus-return', method='Set')

    # Enable the account
    call_async(q, account, 'Set', cs.ACCOUNT, 'Enabled', True,
            dbus_interface=cs.PROPERTIES_IFACE)

    # Set online presence
    presence = dbus.Struct((dbus.UInt32(cs.PRESENCE_TYPE_BUSY), 'busy',
            'Fixing MC bugs'), signature='uss')
    call_async(q, account, 'Set', cs.ACCOUNT,
            'RequestedPresence', presence,
            dbus_interface=cs.PROPERTIES_IFACE)

    e = q.expect('dbus-method-call', method='RequestConnection',
            args=['fakeprotocol', params],
            destination=tp_name_prefix + '.ConnectionManager.fakecm',
            path=tp_path_prefix + '/ConnectionManager/fakecm',
            interface=tp_name_prefix + '.ConnectionManager',
            handled=False)

    conn = SimulatedConnection(q, bus, 'fakecm', 'fakeprotocol', '_',
            'myself', has_presence=True)

    q.dbus_return(e.message, conn.bus_name, conn.object_path, signature='so')

    # MC calls GetStatus (maybe) and then Connect

    q.expect('dbus-method-call', method='Connect',
            path=conn.object_path, handled=True)

    # Connect succeeds
    conn.StatusChanged(cs.CONN_STATUS_CONNECTED, cs.CONN_STATUS_REASON_NONE)

    q.expect('dbus-method-call',
             interface=cs.CONN_IFACE_SIMPLE_PRESENCE,
             method='SetPresence',
             args=list(presence[1:]),
             handled=True)

    # Connection falls over for a miscellaneous reason
    conn.ConnectionError('com.example.My.Network.Is.Full.Of.Eels',
            {'eels': 23, 'capacity': 23, 'debug-message': 'Too many eels'})
    conn.StatusChanged(cs.CONN_STATUS_DISCONNECTED,
            cs.CONN_STATUS_REASON_NETWORK_ERROR)

    # MC reconnects. This time, we expect it to have deleted the 'register'
    # parameter.
    del params['register']

    disconnected, connecting, e = q.expect_many(
            EventPattern('dbus-signal', signal='AccountPropertyChanged',
                predicate=(lambda e:
                    e.args[0].get('ConnectionStatus') ==
                        cs.CONN_STATUS_DISCONNECTED),
                ),
            EventPattern('dbus-signal', signal='AccountPropertyChanged',
                predicate=(lambda e:
                    e.args[0].get('ConnectionStatus') ==
                        cs.CONN_STATUS_CONNECTING),
                ),
            EventPattern('dbus-method-call', method='RequestConnection',
                args=['fakeprotocol', params],
                destination=tp_name_prefix + '.ConnectionManager.fakecm',
                path=tp_path_prefix + '/ConnectionManager/fakecm',
                interface=tp_name_prefix + '.ConnectionManager',
                handled=False),
            )

    assertEquals('/', disconnected.args[0].get('Connection'))
    assertEquals('com.example.My.Network.Is.Full.Of.Eels',
            disconnected.args[0].get('ConnectionError'))
    assertEquals(
            {'eels': 23, 'capacity': 23, 'debug-message': 'Too many eels'},
            disconnected.args[0].get('ConnectionErrorDetails'))
    assertEquals(cs.CONN_STATUS_DISCONNECTED,
        disconnected.args[0].get('ConnectionStatus'))
    assertEquals(cs.CONN_STATUS_REASON_NETWORK_ERROR,
        disconnected.args[0].get('ConnectionStatusReason'))

    assertEquals('/', connecting.args[0].get('Connection'))
    assertEquals('com.example.My.Network.Is.Full.Of.Eels',
            connecting.args[0].get('ConnectionError'))
    assertEquals(
            {'eels': 23, 'capacity': 23, 'debug-message': 'Too many eels'},
            connecting.args[0].get('ConnectionErrorDetails'))
    assertEquals(cs.CONN_STATUS_CONNECTING,
        connecting.args[0].get('ConnectionStatus'))
    assertEquals(cs.CONN_STATUS_REASON_REQUESTED,
        connecting.args[0].get('ConnectionStatusReason'))

    conn = SimulatedConnection(q, bus, 'fakecm', 'fakeprotocol', '_',
            'myself', has_presence=True)

    q.dbus_return(e.message, conn.bus_name, conn.object_path, signature='so')

    # MC calls GetStatus (maybe) and then Connect

    connecting, _ = q.expect_many(
            EventPattern('dbus-signal', signal='AccountPropertyChanged',
                predicate=(lambda e:
                    e.args[0].get('ConnectionStatus') ==
                        cs.CONN_STATUS_CONNECTING),
                ),
            EventPattern('dbus-method-call', method='Connect',
                path=conn.object_path, handled=True),
            )

    assertEquals(conn.object_path, connecting.args[0].get('Connection'))
    assertEquals('com.example.My.Network.Is.Full.Of.Eels',
            connecting.args[0].get('ConnectionError'))
    assertEquals(
            {'eels': 23, 'capacity': 23, 'debug-message': 'Too many eels'},
            connecting.args[0].get('ConnectionErrorDetails'))
    assertEquals(cs.CONN_STATUS_CONNECTING,
        connecting.args[0].get('ConnectionStatus'))
    assertEquals(cs.CONN_STATUS_REASON_REQUESTED,
        connecting.args[0].get('ConnectionStatusReason'))

    assertEquals('com.example.My.Network.Is.Full.Of.Eels',
            account_props.Get(cs.ACCOUNT, 'ConnectionError'))
    assertEquals(
            {'eels': 23, 'capacity': 23, 'debug-message': 'Too many eels'},
            account_props.Get(cs.ACCOUNT, 'ConnectionErrorDetails'))

    # Connect succeeds
    conn.StatusChanged(cs.CONN_STATUS_CONNECTED, cs.CONN_STATUS_REASON_NONE)

    connected, _ = q.expect_many(
            EventPattern('dbus-signal', signal='AccountPropertyChanged',
                predicate=(lambda e:
                    e.args[0].get('ConnectionStatus') ==
                        cs.CONN_STATUS_CONNECTED),
                ),
            EventPattern('dbus-method-call',
                interface=cs.CONN_IFACE_SIMPLE_PRESENCE,
                method='SetPresence',
                args=list(presence[1:]),
                handled=True),
            )

    assertEquals(conn.object_path, connected.args[0].get('Connection'))
    assertEquals('', connected.args[0].get('ConnectionError'))
    assertEquals({}, connected.args[0].get('ConnectionErrorDetails'))
    assertEquals(cs.CONN_STATUS_CONNECTED,
        connected.args[0].get('ConnectionStatus'))
    assertEquals(cs.CONN_STATUS_REASON_REQUESTED,
        connected.args[0].get('ConnectionStatusReason'))

    assertEquals('', account_props.Get(cs.ACCOUNT, 'ConnectionError'))
    assertEquals({}, account_props.Get(cs.ACCOUNT, 'ConnectionErrorDetails'))

if __name__ == '__main__':
    exec_test(test, {})