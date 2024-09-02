
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
    if isinstance(a, int) and isinstance(b, int):
        return a if a > b else b
    if isinstance(a, float) and isinstance(b, float):
        return a if a > b else b
    if isinstance(a, str) and isinstance(b, str):
        if a.replace(".", "", 1).isdigit() and b.replace(".", "", 1).isdigit():
            a = float(a)
            b = float(b)
            return compare_one(a, b)
        elif a.replace(",", "", 1).isdigit() and b.replace(",", "", 1).isdigit():
            a = float(a.replace(",", "."))
            b = float(b.replace(",", "."))
            return compare_one(a, b)
        else:
            a = str(a) if a > b else str(b)
            return a
    else:
        if isinstance(a, int):
            return a if a > b else b
        elif isinstance(a, float):
            return a if a > b else b
        elif isinstance(b, int):
            return b if b > a else a
        elif isinstance(b, float):
            return b if b > a else a
