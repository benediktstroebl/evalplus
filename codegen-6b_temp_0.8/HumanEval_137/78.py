
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
    if a == b:
        return None
    if (type(a) == str):
        a = float(a[:-1])
    if (type(b) == str):
        b = float(b[:-1])
    if isinstance(a, float) and isinstance(b, float):
        return a if a > b else b
    if (type(a) == float):
        return a
    if (type(b) == float):
        return b
    if (type(a) == int):
        return a
    if (type(b) == int):
        return b
    return None


compare_one = compare_one

