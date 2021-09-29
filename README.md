# modelop/test_model_error_on_init

This model will intentionally raise a ZeroDivisionError during the
initialization process to force a ModelOp runtime into an ERROR state.

To test this scenario:

1. Import this model into a MOC instance
2. Add a REST JSON input endpoint to a runtime of your choice.
3. Make a snapshot of this model and REST deploy it to the runtime from step (2).
