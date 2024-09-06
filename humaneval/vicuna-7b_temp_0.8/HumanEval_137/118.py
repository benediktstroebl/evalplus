
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
    if isinstance(a, int) and isinstance(b, int):
        return a > b
    elif isinstance(a, float) and isinstance(b, float):
        return a > b
    elif isinstance(a, str) and isinstance(b, str):
        a = float(a)
        b = float(b)
        return a > b
    elif isinstance(a, str) and not isinstance(b, str):
        return str(a) > str(b)
    elif not isinstance(a, str) and isinstance(b, str):
        return str(a) < str(b)
    elif not isinstance(a, int) and isinstance(b, int):
        return str(a) > str(b)
    elif isinstance(a, int) and not isinstance(b, int):
        return str(a) < str(b)
    else:
        return None
