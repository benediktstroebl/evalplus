def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        return None
    # Check integer
    if type(a) is int and a == b:
        return None
    # Check float
    if type(a) is float and a == b:
        return None
    # Check string
    if type(a) is str:
        x = a.strip('.,')
        y = b.strip('.,')
        if x == y:
            return None
        elif x > y:
            return a
        else:
            return b
    # Unknown type
    return a if a > b else b