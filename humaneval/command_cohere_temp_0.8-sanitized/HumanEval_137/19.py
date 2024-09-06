def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        if issubclass(type(a), str) and issubclass(type(b), str):
            return a if a > b else b
        elif issubclass(type(a), (int, float)) and issubclass(type(b), (int, float)):
            return a if a > b else b
        else:
            return a if type(a) > type(b) else b
    # Check value
    if a == b:
        return None
    return a if a > b else b