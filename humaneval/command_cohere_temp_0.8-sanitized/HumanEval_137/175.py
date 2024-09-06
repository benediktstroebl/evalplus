def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_one.total_tests += 1
    if type(a) is not type(b):
        return None
    if type(a) is int:
        if a >= b:
            return a
        else:
            return b
    if type(a) is float:
        if a >= b:
            return a
        else:
            return b
    if type(a) is str:
        if a.lower() >= b.lower():
            return a
        else:
            return b