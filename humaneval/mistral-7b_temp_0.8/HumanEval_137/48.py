
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

    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            if a > b:
                return a
            else:
                return b
        else:
            return a
    elif type(a) == str and "." in a:
        a = float(a)
    else:
        return a

    if type(b) == int or type(b) == float:
        if type(a) == int or type(a) == float:
            if b > a:
                return b
            else:
                return a
        else:
            return b
    elif type(b) == str and "." in b:
        b = float(b)
    else:
        return b

    if a == b:
        return None

    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return None
    elif type(a) == str:
        if type(b
