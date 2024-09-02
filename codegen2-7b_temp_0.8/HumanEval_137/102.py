
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
    def is_float(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    if is_float(a) and is_float(b):
        return float(a) if float(a) > float(b) else float(b)
    elif is_float(a) or is_float(b):
        return float(a) if is_float(a) else float(b)
    else:
        return str(a) if str(a) > str(b) else str(b
