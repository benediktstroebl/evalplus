
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

    def _compare_one(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if a > b:
                return a
            elif b > a:
                return b
            else:
                return None
        elif isinstance(a, str) and isinstance(b, str):
            if a.isdigit() and b.isdigit():
                return float(a) if float(a) > float(b) else float(b)
            else:
                return a if a > b else b
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return _compare_one(float(b), a)
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return _compare_one(a, float(b))

    return _compare_one(a, b)

