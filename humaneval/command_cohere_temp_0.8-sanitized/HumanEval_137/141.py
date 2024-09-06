def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    # Check if `a` and `b` are of the same type
    if type(a) == type(b):
        if isinstance(a, str):
            a = a.strip()  # Remove trailing . or , if exists
            b = b.strip()  # ...and the other value
        compare_result = float(a) if a == b == "" else a if a > b else b
    return compare_result