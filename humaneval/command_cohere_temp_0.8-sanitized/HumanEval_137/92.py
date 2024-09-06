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
    # Sequential flow for type and value checking
    if isinstance(a, int) and isinstance(b, int):
        return a if a > b else b
    if isinstance(a, float) and isinstance(b, float):
        return a if a > b else b
    if isinstance(a, str) and isinstance(b, str):
        if a.strip('.') < b.strip('.') and a.strip(',') < b.strip(','):
            return a
        return b
    return None