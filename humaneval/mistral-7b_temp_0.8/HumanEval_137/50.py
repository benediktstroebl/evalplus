
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
    if a is not None and b is not None and type(a) is int and type(b) is int:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif a is not None and b is not None and type(a) is int and type(b) is float:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif a is not None and b is not None and type(a) is float and type(b) is float:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif a is not None and b is not None and type(a) is int and type(b) is str:
        if a > float(b):
            return a
        elif a < float(b):
            return float(b)
        else:
            return None
    elif a is not None and b is not None and type(a) is str and type(
