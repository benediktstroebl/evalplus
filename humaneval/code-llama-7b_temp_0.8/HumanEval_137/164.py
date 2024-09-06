
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
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        elif isinstance(b, str):
            if a == float(b.replace(',', '.')):
                return None
            elif a > float(b.replace(',', '.')):
                return a
            else:
                return b
        else:
            return a
    elif isinstance(a, str):
        if isinstance(b, int) or isinstance(b, float):
            if a.replace(',', '.') == b:
                return None
            elif a.replace(',', '.') > b:
                return a
            else:
                return b
        elif isinstance(b, str):
            if a.replace(',', '.') == b.replace(',', '.'):
                return None
            elif a.replace(',', '.') > b.replace(',', '.'):
                return a
            else:
                return b
        else:
            return a
    else:
        return a

