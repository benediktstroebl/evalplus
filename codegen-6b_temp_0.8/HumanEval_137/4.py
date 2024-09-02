
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
    if a == b:
        return None
    elif type(a) is str:
        if a[-1] == ',':
            a = a[:-1]
        a = float(a)
    else:
        a = float(a)
    if type(b) is str:
        if b[-1] == ',':
            b = b[:-1]
        b = float(b)
    else:
        b = float(b)
    if a > b:
        return a
    else:
        return b

