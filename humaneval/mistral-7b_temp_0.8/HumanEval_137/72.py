
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
        if a == b:
            return None
        else:
            return a
    else:
        if type(a) == type(1) and type(b) == type(2.5):
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        elif type(a) == type(1) and type(b) == type("2,3"):
            if a == b:
                return None
            else:
                return b
        elif type(a) == type("2,3") and type(b) == type(1):
            if a == b:
                return None
            else:
                return a
        elif type(a) == type("5,1") and type(b) == type("6"):
            if a == b:
                return None
            else:
                return b
        elif type(a) == type("1") and type(b) == type(1):
            return None

