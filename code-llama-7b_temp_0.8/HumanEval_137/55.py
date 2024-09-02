
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
    a, b = str(a), str(b)
    if a == b:
        return None
    elif len(a) > len(b):
        return a if float(a.replace(",", ".")) > float(b.replace(",", ".")) else b
    elif len(b) > len(a):
        return b if float(b.replace(",", ".")) > float(a.replace(",", ".")) else a
    else:
        return a if float(a.replace(",", ".")) > float(b.replace(",", ".")) else b
