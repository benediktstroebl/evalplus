def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_one.string_check(a, b)

    if type(a) is not type(b):
        if isinstance(a, str) and isinstance(b, str):
            if a == b:
                return None
            return a if a > b else b
        return a if isinstance(a, int) or isinstance(a, float) else b

    return None
def string_check(a, b):
    """
    Check if both inputs are strings, and strip whitespace
    from the beginning and end of strings before continuing.
    """
    a, b = str(a).strip(), str(b).strip()
    return a, b