
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
    # First version
    if type(a) == type(b):
        if a == b:
            return None
        if a > b:
            return a
        return b
    else:
        if a > b:
            return type(a)(a)
        return type(b)(b)

    # Second version
    if type(a) == type(b):
        if a == b:
            return None
        if a > b:
            return a
        return b
    else:
        try:
            if a > b:
                return type(a)(a)
            return type(b)(b)
        except TypeError:
            return None


    # Third version
    try:
        if a > b:
            return type(a)(a)
        return type(b)(b)
    except TypeError:
        return None
