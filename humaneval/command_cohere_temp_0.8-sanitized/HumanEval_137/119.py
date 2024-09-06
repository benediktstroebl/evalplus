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
        # If the types are different, return the larger value with its type
        if isinstance(a, int) and isinstance(b, str) and float(b) > a:
            return b
        elif isinstance(b, int) and isinstance(a, str) and float(a) > b:
            return a
        elif isinstance(a, float) and isinstance(b, str) and float(b) > a:
            return b
        elif isinstance(b, float) and isinstance(a, str) and float(a) > b:
            return a
        elif isinstance(a, str) and isinstance(b, int):
            return a
        elif isinstance(a, str) and isinstance(b, float):
            return a
        elif isinstance(b, str) and isinstance(a, int):
            return b
        elif isinstance(b, str) and isinstance(a, float):
            return b
    elif a == b:
        return None
    else:
        return a if a > b else b