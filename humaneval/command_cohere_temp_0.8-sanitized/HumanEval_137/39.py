def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_val = None
    if type(a) == type(b) and type(a) in [int, float, str]:
        if isinstance(a, str):
            a = float(a)
        elif isinstance(a, int) or isinstance(a, float):
            a = float(a)
        compare_val = max(a, b)
    return compare_val