
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

    if type(a) == type(b):
        if a < b:
            return b
        elif a == b:
            return None
        else:
            return a
    elif type(a) == int and type(b) == float:
        if a < b:
            return round(b,2)
        elif a == b:
            return None
        else:
            return round(a,2)
    elif type(a) == float and type(b) == int:
        if a < b:
            return round(a,2)
        elif a == b:
            return None
        else:
            return round(b,2)
    elif type(a) == float:
        if a < b:
            return round(b,2)
        elif a == b:
            return None
        else:
            return round(a,2)
    elif type(b) == float:
        if a < b:
            return round(b,2)
        elif a == b:
            return None
        else:
            return round(a,2)
