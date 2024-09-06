
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if type(a) != type(b):
        return None
    elif isinstance(a, int):
        if isinstance(b, basestring):
            if "," in b:
                return float(b)
            else:
                return int(b)
        elif isinstance(b, int) or isinstance(b, float):
            return b
    elif isinstance(a, float):
        if isinstance(b, basestring):
            if "," in b:
                return float(b)
            else:
                return int(b)
        elif isinstance(b, int) or isinstance(b, float):
            return b
    elif isinstance(a, basestring):
        if isinstance(b, basestring):
            if "," in a:
                return float(a)
            else:
                return int(a)
        elif isinstance(b, int) or isinstance(b, float):
            return b

