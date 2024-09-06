
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
    if not isinstance(a, (float, int, str)) or not isinstance(b, (float, int, str)):
        raise TypeError('Inputs must be numbers')

    if isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, float):
        return b
    elif isinstance(b, float):
        return a
    elif isinstance(a, str) or isinstance(b, str):
        return a if float(a) > float(b) else b
    else:
        return
