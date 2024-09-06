def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # check type of a and b, needed for python 3.7 and higher
    if type(a) is not type(b):
        if isinstance(a, float) and isinstance(b, str) or isinstance(b, float) and isinstance(a, str):
            return "%.2f" % (float(a) if isinstance(a, str) else a)
        elif isinstance(a, str) and isinstance(b, str):
            return a if a == b else None
        else:
            return str(a) if isinstance(a, int) or isinstance(a, float) else a
    elif a == b:
        return None
    elif a > b:
        return a
    else:
        return b