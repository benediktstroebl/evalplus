def multiply(a, b):
    """Returns the product of the unit digits of the inputted integers."""
    return int(str(a)[-1]) * int(str(b)[-1])