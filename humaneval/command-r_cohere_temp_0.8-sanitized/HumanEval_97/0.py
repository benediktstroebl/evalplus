def multiply(a, b):
    """Returns the product of the unit digits of two integers."""
    return int(str(a)[-1] * str(b)[-1])