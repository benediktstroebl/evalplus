
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
    if not isinstance(a, type(b)) and not isinstance(b, type(a)):
        if not a and not b:
            return None
        elif not a:
            return b
        else:
            return a
    elif isinstance(a, str) and isinstance(b, str):
        a = re.sub(",", "", a)
        b = re.sub(",", "", b)
        return float(a) > float(b) or float(b) > float(a)
    else:
        return a > b

