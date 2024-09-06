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
        if isinstance(a, str):  # If the variables are strings
            compare_result = max(a.replace('.', ','), b.replace('.', ','))
        else:
            compare_result = max(a, b)
    elif isinstance(a, str) and isinstance(b, (int, float)):
        compare_result = a
    elif isinstance(a, (int, float)) and isinstance(b, str):
        compare_result = b
    return compare_result