
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

    if isinstance(a, str) and isinstance(b, str):
        a, b = a.replace(",", "."), b.replace(",", ".")
        if float(a) > float(b):
            return a
        elif float(a) < float(b):
            return b
    elif isinstance(a, str) and not isinstance(b, str):
        a, b = float(a), b
        if float(a) > b:
            return a
        elif float(a) < b:
            return b
    elif isinstance(b, str) and not isinstance(a, str):
        a, b = a, float(b)
        if float(a) > b:
            return a
        elif float(a) < b:
            return b
    elif float(a) > float(b):
        return a
    elif float(a) < float(b):
        return b
    return None
