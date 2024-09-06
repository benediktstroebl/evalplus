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
        # If the types are different, return the larger value with its original type
        if isinstance(a, int) and isinstance(b, float):
            return b
        elif isinstance(a, float) and isinstance(b, int):
            return a
        elif isinstance(a, str) and (isinstance(b, int or float)):
            return a
        elif isinstance(b, str) and (isinstance(a, int or float)):
            return b
        else:
            return None  # Wrong input, this should never happen since we check int and float beforehand

    # If types are the same, compare the values
    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b