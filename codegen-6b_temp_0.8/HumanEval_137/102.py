
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
        elif type(a) is int:
            if type(b) is float:
                return b
            elif type(b) is str:
                return eval(b)
        elif type(a) is str:
            if type(b) is float:
                return eval(a)
            elif type(b) is str:
                return None
        elif type(a) is float:
            if type(b) is str:
                return eval(a)
            elif type(b) is float:
                return eval(str(a) + ', ' + str(b))
        elif type(a) is str:
            if type(b) is int:
                return eval(a)
            elif type(b) is float:
                return eval(str(b) + ', ' + a)

    else:
        return None
    print(None)
