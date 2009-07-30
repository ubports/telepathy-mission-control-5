
#ifndef __mc_signals_marshal_MARSHAL_H__
#define __mc_signals_marshal_MARSHAL_H__

#include	<glib-object.h>

G_BEGIN_DECLS

/* VOID:STRING,STRING (mc-signals-marshal.list:1) */
extern void mc_signals_marshal_VOID__STRING_STRING (GClosure     *closure,
                                                    GValue       *return_value,
                                                    guint         n_param_values,
                                                    const GValue *param_values,
                                                    gpointer      invocation_hint,
                                                    gpointer      marshal_data);

/* VOID:UINT,UINT,STRING,STRING (mc-signals-marshal.list:2) */
extern void mc_signals_marshal_VOID__UINT_UINT_STRING_STRING (GClosure     *closure,
                                                              GValue       *return_value,
                                                              guint         n_param_values,
                                                              const GValue *param_values,
                                                              gpointer      invocation_hint,
                                                              gpointer      marshal_data);

/* VOID:UINT,STRING (mc-signals-marshal.list:3) */
extern void mc_signals_marshal_VOID__UINT_STRING (GClosure     *closure,
                                                  GValue       *return_value,
                                                  guint         n_param_values,
                                                  const GValue *param_values,
                                                  gpointer      invocation_hint,
                                                  gpointer      marshal_data);

/* VOID:UINT,UINT (mc-signals-marshal.list:4) */
extern void mc_signals_marshal_VOID__UINT_UINT (GClosure     *closure,
                                                GValue       *return_value,
                                                guint         n_param_values,
                                                const GValue *param_values,
                                                gpointer      invocation_hint,
                                                gpointer      marshal_data);

/* VOID:UINT,BOOLEAN (mc-signals-marshal.list:5) */
extern void mc_signals_marshal_VOID__UINT_BOOLEAN (GClosure     *closure,
                                                   GValue       *return_value,
                                                   guint         n_param_values,
                                                   const GValue *param_values,
                                                   gpointer      invocation_hint,
                                                   gpointer      marshal_data);

/* VOID:BOXED,BOXED (mc-signals-marshal.list:6) */
extern void mc_signals_marshal_VOID__BOXED_BOXED (GClosure     *closure,
                                                  GValue       *return_value,
                                                  guint         n_param_values,
                                                  const GValue *param_values,
                                                  gpointer      invocation_hint,
                                                  gpointer      marshal_data);

/* VOID:BOXED,STRING (mc-signals-marshal.list:7) */
extern void mc_signals_marshal_VOID__BOXED_STRING (GClosure     *closure,
                                                   GValue       *return_value,
                                                   guint         n_param_values,
                                                   const GValue *param_values,
                                                   gpointer      invocation_hint,
                                                   gpointer      marshal_data);

/* VOID:STRING,BOOLEAN (mc-signals-marshal.list:8) */
extern void mc_signals_marshal_VOID__STRING_BOOLEAN (GClosure     *closure,
                                                     GValue       *return_value,
                                                     guint         n_param_values,
                                                     const GValue *param_values,
                                                     gpointer      invocation_hint,
                                                     gpointer      marshal_data);

G_END_DECLS

#endif /* __mc_signals_marshal_MARSHAL_H__ */

