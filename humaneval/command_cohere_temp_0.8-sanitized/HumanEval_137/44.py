def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    if isinstance(a, int) and isinstance(b, int):
        compare_result = max(a, b)
    elif isinstance(a, float) and isinstance(b, (int, float)):
        compare_result = max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        compare_result = a if a.strip('.,').isdigit() >= b.strip('.,').isdigit() else b
    return compare_result