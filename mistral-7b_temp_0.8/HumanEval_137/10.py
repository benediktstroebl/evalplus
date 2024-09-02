
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
    elif isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            if a < b:
                return b
            elif a > b:
                return a
        elif isinstance(b, str):
            if a < float(b):
                return float(b)
            elif a > float(b):
                return a
    elif isinstance(a, str):
        if isinstance(b, (int, float)):
            if float(a) < b:
                return b
            elif float(a) > b:
                return float(a)
        elif isinstance(b, str):
            if float(a) < float(b):
                return float(b)
            elif float(a) > float(b):
                return float(a)

    return None

