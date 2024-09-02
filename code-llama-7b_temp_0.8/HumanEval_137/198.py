
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

    a = str(a)
    b = str(b)

    a = a.replace(".", "").replace(",", "")
    b = b.replace(".", "").replace(",", "")

    if len(a) < len(b):
        a, b = b, a

    if a > b:
        if a.isdigit():
            return int(a)
        else:
            return float(a)
    elif a < b:
        if b.isdigit():
            return int(b)
        else:
            return float(b)
    else:
        return None
