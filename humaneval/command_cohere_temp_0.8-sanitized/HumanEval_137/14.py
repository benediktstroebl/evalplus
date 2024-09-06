def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare = None
    if isinstance(a, int) and isinstance(b, int):
        compare = a if a > b else b
    elif isinstance(a, float) and isinstance(b, float):
        compare = a if a > b else b
    elif isinstance(a, str) and isinstance(b, str):
        compare = a if a > b else b
    elif isinstance(a, (int, float)) and isinstance(b, str):
        compare = b if float(b) > a else a
    elif isinstance(a, str) and isinstance(b, (int, float)):
        compare = a if float(a) > b else b
    return compare