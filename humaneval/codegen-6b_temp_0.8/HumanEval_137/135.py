
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
    elif type(a) == float or type(b) == float:
        if float(a) > float(b):
            return float(a)
        return float(b)
    elif type(a) == int or type(b) == int:
        if int(a) > int(b):
            return int(a)
        return int(b)
    elif type(a) == str:
        if float(a) > float(b):
            return float(a)
        return float(b)
    elif type(a) == str:
        if int(a) > int(b):
            return int(a)
        return int(b)
    else:
        return None

