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
        # If the types are different, ensure that the return value is of the
        #  same type as the first parameter 'a'
        if isinstance(a, (int, float)):
            return float(b) if b > a else None
        elif isinstance(a, str):
            return str(b) if b > a else None
    elif a == b:
        return None
    else:
        return a if a > b else b