
/* Generated data (by glib-mkenums) */

#include "mcd-enum-types.h"
#define g_intern_static_string(s) (s)

/* enumerations from "mcd-mission.h" */
GType
mcd_mode_get_type (void)
{
  static GType etype = 0;
  if (etype == 0) {
    static const GEnumValue values[] = {
      { MCD_MODE_UNKNOWN, "MCD_MODE_UNKNOWN", "unknown" },
      { MCD_MODE_NORMAL, "MCD_MODE_NORMAL", "normal" },
      { MCD_MODE_RESTRICTED, "MCD_MODE_RESTRICTED", "restricted" },
      { MCD_MODE_CALL, "MCD_MODE_CALL", "call" },
      { 0, NULL, NULL }
    };
    etype = g_enum_register_static (g_intern_static_string ("McdMode"), values);
  }
  return etype;
}
GType
mcd_system_flags_get_type (void)
{
  static GType etype = 0;
  if (etype == 0) {
    static const GFlagsValue values[] = {
      { MCD_SYSTEM_CONNECTED, "MCD_SYSTEM_CONNECTED", "connected" },
      { MCD_SYSTEM_MEMORY_CONSERVED, "MCD_SYSTEM_MEMORY_CONSERVED", "memory-conserved" },
      { MCD_SYSTEM_POWER_CONSERVED, "MCD_SYSTEM_POWER_CONSERVED", "power-conserved" },
      { MCD_SYSTEM_SCREEN_BLANKED, "MCD_SYSTEM_SCREEN_BLANKED", "screen-blanked" },
      { MCD_SYSTEM_LOCKED, "MCD_SYSTEM_LOCKED", "locked" },
      { MCD_SYSTEM_IDLE, "MCD_SYSTEM_IDLE", "idle" },
      { 0, NULL, NULL }
    };
    etype = g_flags_register_static (g_intern_static_string ("McdSystemFlags"), values);
  }
  return etype;
}

/* enumerations from "mcd-channel.h" */
GType
mcd_channel_status_get_type (void)
{
  static GType etype = 0;
  if (etype == 0) {
    static const GEnumValue values[] = {
      { MCD_CHANNEL_STATUS_UNDISPATCHED, "MCD_CHANNEL_STATUS_UNDISPATCHED", "undispatched" },
      { MCD_CHANNEL_STATUS_REQUEST, "MCD_CHANNEL_STATUS_REQUEST", "request" },
      { MCD_CHANNEL_STATUS_REQUESTED, "MCD_CHANNEL_STATUS_REQUESTED", "requested" },
      { MCD_CHANNEL_STATUS_DISPATCHING, "MCD_CHANNEL_STATUS_DISPATCHING", "dispatching" },
      { MCD_CHANNEL_STATUS_HANDLER_INVOKED, "MCD_CHANNEL_STATUS_HANDLER_INVOKED", "handler-invoked" },
      { MCD_CHANNEL_STATUS_DISPATCHED, "MCD_CHANNEL_STATUS_DISPATCHED", "dispatched" },
      { MCD_CHANNEL_STATUS_FAILED, "MCD_CHANNEL_STATUS_FAILED", "failed" },
      { 0, NULL, NULL }
    };
    etype = g_enum_register_static (g_intern_static_string ("McdChannelStatus"), values);
  }
  return etype;
}

/* enumerations from "mcd-transport.h" */
GType
mcd_transport_status_get_type (void)
{
  static GType etype = 0;
  if (etype == 0) {
    static const GEnumValue values[] = {
      { MCD_TRANSPORT_STATUS_CONNECTED, "MCD_TRANSPORT_STATUS_CONNECTED", "connected" },
      { MCD_TRANSPORT_STATUS_CONNECTING, "MCD_TRANSPORT_STATUS_CONNECTING", "connecting" },
      { MCD_TRANSPORT_STATUS_DISCONNECTED, "MCD_TRANSPORT_STATUS_DISCONNECTED", "disconnected" },
      { MCD_TRANSPORT_STATUS_DISCONNECTING, "MCD_TRANSPORT_STATUS_DISCONNECTING", "disconnecting" },
      { 0, NULL, NULL }
    };
    etype = g_enum_register_static (g_intern_static_string ("McdTransportStatus"), values);
  }
  return etype;
}

/* enumerations from "mcd-provisioning.h" */
GType
mcd_provisioning_error_get_type (void)
{
  static GType etype = 0;
  if (etype == 0) {
    static const GEnumValue values[] = {
      { MCD_PROVISIONING_ERROR_NOT_FOUND, "MCD_PROVISIONING_ERROR_NOT_FOUND", "not-found" },
      { MCD_PROVISIONING_ERROR_NO_RESPONSE, "MCD_PROVISIONING_ERROR_NO_RESPONSE", "no-response" },
      { MCD_PROVISIONING_ERROR_BAD_RESULT, "MCD_PROVISIONING_ERROR_BAD_RESULT", "bad-result" },
      { 0, NULL, NULL }
    };
    etype = g_enum_register_static (g_intern_static_string ("McdProvisioningError"), values);
  }
  return etype;
}

#define __MCD_ENUM_TYPES_C__

/* Generated data ends here */

