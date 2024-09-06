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
    # Check value
    if a == b:
        return None
    # Determine return based on type and value
    if type(a) is int and a > b:
        return a
    elif type(a) is float and a > b or str(a).replace(",", "", 1) > str(b).replace(",", "", 1):
        return a
    elif type(a) is str and a > b:
        return a
    else:
        return b