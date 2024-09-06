def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type and return a if it is different from b
    if type(a) != type(b):
        return a if is_numeric(a) and is_numeric(b) else a

    # Check value and return the larger one
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None
def is_numeric(n):
    return isinstance(n, (int, float, str))