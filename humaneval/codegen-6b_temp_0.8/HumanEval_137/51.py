
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
    try:
        a = float(a)
    except:
        a = type('a', (object,), {'__init__': lambda self, a: None})
        a.__init__(a, a)
    try:
        b = float(b)
    except:
        b = type('b', (object,), {'__init__': lambda self, b: None})
        b.__init__(b, b)
    if a > b:
        return a
    else:
        return b

