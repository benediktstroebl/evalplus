
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
    if isinstance(a, float) or isinstance(a, int) and a.is_integer() or isinstance(a, str):
        if isinstance(b, float) or isinstance(b, int) and b.is_integer() or isinstance(b, str):
            if a > b:
                return a
            elif a < b:
                return -b
            else:
                return None
    elif isinstance(a, str) and isinstance(b, str):
        if a.isdigit() and not b.isdigit():
            return -float(b)
        elif b.isdigit() and not a.isdigit():
            return float(a)
        else:
            return None
    elif isinstance(a, list) or isinstance(b, list):
        if len(a) > len(b):
            return a
        else:
            return b
    else:
        return None
