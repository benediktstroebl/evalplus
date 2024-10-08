
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
        else:
            return a
    if type(a) == float and type(b) == float:
        if a < b:
            return b
        else:
            return a
    if type(a) == str and type(b) == str:
        a = float(a)
        b = float(b)
        if a < b:
            return b
        else:
            return a
    if type(a) == float:
        if a < b:
            return b
        else:
            return a
    if type(b) == float:
        if a < b:
            return b
        else:
            return a
    if type(a) == str and type(b) == int:
        a = float(a)
        if a < b:
            return b
        else:
            return a
    if type(a) == int and type(b) == str:
        b = float(b)
        if a < b:
            return b
