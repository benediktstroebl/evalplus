def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_one.turned_into_none = 0
    compare_one.a = a
    compare_one.b = b
    if type(a) is not type(b):
        if isinstance(a, str) and '.' in a and isinstance(b, int):
            compare_one.a = float(a)
        elif isinstance(b, str) and '.' in b and isinstance(a, int):
            compare_one.b = float(b)
        elif isinstance(a, str) and ',' in a and isinstance(b, float):
            compare_one.a = str(a)
        elif isinstance(b, str) and ',' in b and isinstance(a, float):
            compare_one.b = str(b)
        elif isinstance(a, str) and ',' in a and isinstance(b, str):
            compare_one.a = str(a)
        elif isinstance(b, str) and ',' in b and isinstance(a, str):
            compare_one.b = str(b)
        else:
            return b if type(b) is int or type(b) is float else None
    elif a == b:
        return None
    elif isinstance(a, int) or isinstance(a, float):
        return a
    else:
        return a