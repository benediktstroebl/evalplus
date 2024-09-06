def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_val = None
    if isinstance(a, int) and isinstance(b, int):
        compare_val = a if a > b else b
    elif isinstance(a, float) and isinstance(b, float):
        compare_val = a if a > b else b
    elif isinstance(a, str) and isinstance(b, str):
        compare_val = a if a > b else b
    elif isinstance(a, (int, float)) and isinstance(b, str):
        compare_val = b
    elif isinstance(a, str) and isinstance(b, (int, float)):
        compare_val = a
    return compare_val