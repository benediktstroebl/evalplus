
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
    # Check the variable types
    if a is None or b is None:
        return None
    elif isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, str) and isinstance(b, str):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    else:
        raise ValueError("Invalid input type")
