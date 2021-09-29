"""
modelop/test_model_error_on_init

This model will intentionally raise a ZeroDivisionError during the
initialization process to force a ModelOp runtime into an ERROR state.
"""

# modelop.init
def begin():
    """Intentionally divide by 0 to set the runtime into an ERROR state"""
    my_failure = 1 / 0
    pass


# modelop.score
def action(datum):
    """An echo model"""
    yield datum


# modelop.metrics
def metrics(data):
    """Yields a basic dictionary"""
    yield {"metrics": 1.0}
