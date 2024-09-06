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
    if type(a) is not type(b):
        return None
    elif type(a) is int and a == b:
        return None
    elif type(a) is float and a == b:
        return None
    elif type(a) is str and a == b:
        return None
    elif isinstance(a, int) and isinstance(b, int):
        return b
    elif isinstance(a, float) and isinstance(b, float):
        return b
    elif isinstance(a, str) and isinstance(b, str):
        if a.find('.') >= 0 and b.find('.') >= 0:
            return a if float(a) > float(b) else b
        elif a.find(',') >= 0 and b.find(',') >= 0:
            return a if float(a) > float(b) else b
        else:
            return a if int(a) > int(b) else b