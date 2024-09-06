
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
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            if a > b:
                return a
            elif a < b:
                return b
        elif isinstance(b, (int, float)) and b.lower() == str(b):
            if a > float(b):
                return a
            elif a < float(b):
                return float(b)
        elif isinstance(b, (int, float)) and b.upper() == str(b):
            if a > float(b):
                return a
            elif a < float(b):
                return float(b)
        return None
    elif isinstance(a, str) and isinstance(b, str):
        if a.lower() == b.lower():
            if a.isdigit() < b.isdigit():
                return a
            else:
                return b
        elif a.upper() == b.upper():
            if a.isdigit() < b.isdigit():
                return a
            else:
                return b
        return None
    elif isinstance(a, str) and isinstance(b, int):
        if a.lower() == b.lower():
            if a.isdigit() < b:
                return a
            else:
                return b
        elif a.upper() == b.upper():
            if a.isdigit() < b:
                return a
            else:
                return b
        return None
    return None
