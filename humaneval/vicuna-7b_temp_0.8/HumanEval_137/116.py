
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
    if isinstance(a, float) and isinstance(b, float):
        if a > b:
            return b
        else:
            return a
    elif isinstance(a, int) and isinstance(b, int):
        if a > b:
            return b
        else:
            return a
    elif isinstance(a, str) and isinstance(b, str):
        if a.isdigit() and b.isdigit():
            if a.replace('.', ',') > b.replace('.', ','):
                return b
            else:
                return a
        elif b.isdigit() and a.isdigit():
            if b.replace('.', ',') > a.replace('.', ','):
                return a
            else:
                return b
        else:
            if a > b:
                return b
            else:
                return a
    else:
        if a > b:
            return b
        else:
            return a
