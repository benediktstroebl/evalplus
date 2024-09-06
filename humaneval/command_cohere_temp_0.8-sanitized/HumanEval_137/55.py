def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_one.mirror = None
    if type(a) is not type(b):
        if type(a) is int:
            return a
        elif type(b) is int:
            return b
        elif type(a) is float:
            return a
        elif type(b) is float:
            return b
        elif a == b:
            return compare_one.mirror
        else:
            return str(a)
    else:
        if a == b:
            return compare_one.mirror
        else:
            return None