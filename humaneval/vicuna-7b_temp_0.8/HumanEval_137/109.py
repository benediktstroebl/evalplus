
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
        if a.isdigit() and int(a) > b:
            return int(a)
        elif b.isdigit() and int(b) > int(a):
            return int(b)
        else:
            return None
    elif type(b) == str and type(a) == float:
        if b.isdigit() and int(b) > int(a):
            return int(b)
        elif int(a) > int(b):
            return int(a)
        else:
            return None
    else:
        return None
