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
    # Determine largest value based on type
    if type(a) is int and type(b) is int:
        return a if a > b else b
    elif type(a) is float and type(b) is float:
        return a if a > b else b
    elif type(a) is str and type(b) is str:
        if a.strip('.,') > b.strip('.,'):
            return a
        else:
            return b
    else:
        return "Error!"