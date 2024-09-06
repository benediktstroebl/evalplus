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
        # If the types are different, return the largest size
        if isinstance(a, float) and isinstance(b, str):
            return b
        elif isinstance(a, str) and isinstance(b, float):
            return a
        elif isinstance(a, int) and isinstance(b, str):
            return b
        elif isinstance(a, str) and isinstance(b, int):
            return a
        else:
            return "Error"
    elif a == b:
        return None
    elif a > b:
        return a
    else:
        return b
a = compare_one(1, 2.5)
b = compare_one(1, "2,3")