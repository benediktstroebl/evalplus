
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
    elif a > b:
        if type(a) is int or type(a) is float:
            return a
        elif type(a) is str:
            if ',' in a:
                return a.replace(',', '.')
            else:
                return a
    elif a < b:
        if type(b) is int or type(b) is float:
            return b
        elif type(b) is str:
            if ',' in b:
                return b.replace(',', '.')
            else:
                return b

