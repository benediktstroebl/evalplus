
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
    v1, v2 = None, None
    if isinstance(a, str):
        v1 = float(a.replace(",", "."))
    else:
        v1 = a
    if isinstance(b, str):
        v2 = float(b.replace(",", "."))
    else:
        v2 = b
    if v1 >= v2:
        return v1
    else:
        return v2

