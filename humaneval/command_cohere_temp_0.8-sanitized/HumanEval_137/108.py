def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        if isinstance(a, str) and isinstance(b, str):
            return a if a > b else b
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return b
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return a
        else:
            return None

    # Compare value
    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b