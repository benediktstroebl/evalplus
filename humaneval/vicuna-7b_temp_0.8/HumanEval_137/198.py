
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
    elif type(a) != type(b):
        if type(a) == str and type(b) == float:
            if float(a) > float(b):
                return float(a)
            elif float(a) < float(b):
                return float(b)
        elif type(b) == str and type(a) == float:
            if float(b) > float(a):
                return float(b)
            elif float(b) < float(a):
                return float(a)
        elif str(a)[0] == str(b)[0] and str(a)[1:] > str(b)[1:]:
            return str(a)[1:]
        elif str(b)[0] == str(a)[0] and str(b)[1:] > str(a)[1:]:
            return str(b)[1:]
        else:
            return None
    else:
        return None
