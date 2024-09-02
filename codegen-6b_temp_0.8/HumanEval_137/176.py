
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
    try:
        r1 = float(a)
    except ValueError:
        try:
            r1 = float(a.replace(',', ''))
        except ValueError:
            r1 = None
    try:
        r2 = float(b)
    except ValueError:
        try:
            r2 = float(b.replace(',', ''))
        except ValueError:
            r2 = None
    if r1 is None and r2 is None:
        return None
    elif r1 is None:
        return r2
    elif r2 is None:
        return r1
    elif r1 > r2:
        return r1
    else:
        return r2

