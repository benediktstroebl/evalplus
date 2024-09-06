
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
    if isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif isinstance(a, float) or isinstance(b, float):
        return float(a) > float(b)
    elif isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif isinstance(a, string) and isinstance(b, string):
        return b.replace('.', ',') > a.replace('.', ',')
    elif isinstance(a, string) or isinstance(b, string):
        return len(a) > len(b)
    else:
        return None

a = [compare_one(i, i) for i in range(1, 6)]
print(a)
