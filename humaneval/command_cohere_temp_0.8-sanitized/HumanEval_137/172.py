def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    if type(a) == type(b) and type(a) in [int, float, str]:
        if type(a) == str:
            a = float(a.replace(",", ".") * 1)
            b = float(b.replace(",", ".") * 1)
        if a > b:
            compare_result = a
        elif a < b:
            compare_result = b
    return compare_result