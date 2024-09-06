
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

    if a==b:
        return None
    else:
        if isinstance(a, float):
            if isinstance(b, float):
                if a>b:
                    return a
                else:
                    return b
            elif isinstance(b, int):
                return a
        elif isinstance(a, int):
            if isinstance(b, int):
                if a>b:
                    return a
                else:
                    return b
            elif isinstance(b, float):
                return b
        elif isinstance(a, str):
            if isinstance(b, str):
                if float(a)<float(b):
                    return b
                else:
                    return a
            elif isinstance(b, int):
                return float(a)
        elif isinstance(b, str):
            if isinstance(a, int):
                return float(b)
            elif isinstance(a, float):
                return float(b)
        elif isinstance(b, float):
            if isinstance(a, int):
                return float(a
