
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
    int_a, float_a, str_a = isinstance(a, int), isinstance(a, float), isinstance(a, str)
    int_b, float_b, str_b = isinstance(b, int), isinstance(b, float), isinstance(b, str)
    if int_a and int_b:
        return max(a, b)
    elif float_a and float_b:
        return max(a, b)
    elif str_a and str_b:
        n_a, n_b = len(a), len(b)
        if n_a > n_b:
            return a
        else:
            return b
    else:
        return None

