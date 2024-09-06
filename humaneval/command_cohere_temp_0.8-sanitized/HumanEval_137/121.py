def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if isinstance(a, float) and isinstance(b, float):
        return a if a > b else b
    elif isinstance(a, int) and isinstance(b, int):
        return a if a > b else b
    elif isinstance(a, str) and isinstance(b, str):
        return a if a > b else b
    return None