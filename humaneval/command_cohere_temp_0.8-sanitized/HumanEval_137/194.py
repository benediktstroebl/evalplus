def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_one.string_number = False
    compare_one.a = None
    compare_one.b = None
    if type(a) is not type(b):
        if isinstance(a, str) and isinstance(b, str):
            compare_one.string_number = True
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            compare_one.a = max(a, b)
        elif isinstance(a, str) and isinstance(b, (int, float)):
            compare_one.a = a
        elif isinstance(a, (int, float)) and isinstance(b, str):
            compare_one.a = b
        else:
            return "ERROR: MISSING CASE"
    elif a == b:
        return None
    else:
        if isinstance(a, str) and isinstance(b, str):
            compare_one.a = a if compare_one.string_number else max(a, b)
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            compare_one.a = max(a, b)
        elif isinstance(a, str) and isinstance(b, (int, float)):
            compare_one.a = b
        elif isinstance(a, (int, float)) and isinstance(b, str):
            compare_one.a = a
        else:
            return "ERROR: MISSING CASE"
    return compare_one.a