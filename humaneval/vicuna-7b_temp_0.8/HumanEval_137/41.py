
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
        else:
            return b
    elif type(a) == str and type(b) == float:
        if a.isnumeric() and b.isnumeric():
            try:
                float(a)
                float(b)
                return a > b
            except ValueError:
                return b > a
        else:
            return b
    elif type(b) == str and type(a) == float:
        return a > b
    else:
        return None
