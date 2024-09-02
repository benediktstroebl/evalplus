
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
    if isinstance(a, int) and isinstance(b, int):
        return b if a > b else a
    elif isinstance(a, float) and isinstance(b, float):
        return b if a > b else a
    elif isinstance(a, str) and isinstance(b, str):
        a, b = a.replace(",", "."), b.replace(",", ".")
        return b if float(a) > float(b) else a
    elif isinstance(a, int) and isinstance(b, float):
        return a if a > b else b
    elif isinstance(a, float) and isinstance(b, int):
        return b if a > b else a
    elif isinstance(a, str) and isinstance(b, float):
        a = a.replace(",", ".")
        return b if float(a) > b else a
    elif isinstance(a, int) and isinstance(b, str):
        return a if a > float(b) else b
    elif isinstance(a, float) and isinstance(b, str):
        b = b.replace(",", ".")
        return a if a > float(b) else b
    elif isinstance(a, str) and isinstance(b, str):
        a, b = a.replace(",", "."), b.replace(",", ".")
        return a if float(a) > float(b) else b
    else:
        return None

