
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

    # String formated to numbers
    if type(a) is str:
        if a.find(',') > 0:
            a = float(a.replace(',', '.'))
        else:
            a = int(a)
    else:
        a = a

    if type(b) is str:
        if b.find(',') > 0:
            b = float(b.replace(',', '.'))
        else:
            b = int(b)
    else:
        b = b

    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b

