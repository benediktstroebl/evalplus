
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
    elif isinstance(a, numbers.Number) or isinstance(b, numbers.Number):
        if a > b:
            return a
        elif b > a:
            return b
    elif isinstance(a, str) or isinstance(b, str):
        if a.isdigit() and b.isdigit():
            return float(a) > float(b)
        elif a == b:
            return None
        else:
            return float(a) > float(b)
    else:
        raise ValueError("Invalid input")
