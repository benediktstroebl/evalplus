
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
    if isinstance(a, float) or isinstance(a, string):
        if isinstance(b, float) or isinstance(b, string):
            if isinstance(a, string) and isinstance(b, string):
                return float(a) > float(b)
            elif isinstance(a, float):
                return float(a) > float(b)
            elif isinstance(b, float):
                return float(b) > float(a)
            else:
                return str(a) > str(b)
        else:
            return float(a) > float(b)
    elif isinstance(a, int) and isinstance(b, int):
        return a > b
    else:
        return None
