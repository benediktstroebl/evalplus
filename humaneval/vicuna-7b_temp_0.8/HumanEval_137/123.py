
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
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == str and type(b) == float:
        if a.isdigit() and b == float(a):
            return float(a)
        elif b.isdigit() and b == float(b):
            return float(b)
        else:
            return None
    elif type(a) == str and type(b) == int:
        if a.isdigit() and b == int(a):
            return int(b)
        elif b.isdigit() and b == int(b):
            return int(a)
        else:
            return None
    elif type(a) == int and type(b) == float:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == int and type(b) == int:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    else:
        return None
