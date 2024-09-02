
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

    if a is None or b is None:
        return None
    if type(a) == type(b):
        if a > b:
            return a
        if b > a:
            return b
        else:
            return None
    if type(a) == str and type(b) == str:
        try:
            a = float(a)
            b = float(b)
        except:
            return None
    if type(a) == str:
        try:
            a = float(a)
        except:
            return None
    if type(b) == str:
        try:
            b = float(b)
        except:
            return None
    return None


