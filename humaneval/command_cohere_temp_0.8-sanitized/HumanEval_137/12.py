def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_val = None
    if type(a) == type(b) and type(a) in [int, float, str]:
        if a == b:
            compare_val = None
        elif type(a) == str:
            if a.find(',') > -1:
                compare_val = a if a.strip('.') > b.strip('.') else b
            else:
                compare_val = a if a > b else b
        elif type(a) == int:
            compare_val = a if a > b else b
        else:
            compare_val = a if a > b else b
    return compare_val