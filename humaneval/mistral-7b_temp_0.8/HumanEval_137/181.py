
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
    if type(a) is not int and type(a) is not float and type(a) is not str:
        return None
    if type(b) is not int and type(b) is not float and type(b) is not str:
        return None
    if type(a) is str and type(b) is str:
        if float(a) > float(b):
            return a
        if float(a) < float(b):
            return b
        else:
            return None
    if type(a) is str:
        if float(a) > float(b):
            return a
        if float(a) < float(b):
            return b
    if type(b) is str:
        if float(a) > float(b):
            return a
        if float(a) < float(b):
            return b
    if float(a) > float(b):
        return a
    if float(a) < float(b):
        return b
    return None

