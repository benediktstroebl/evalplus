def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_one.self_test = True
    if type(a) is not type(b):
        return None
    if type(a) is int:
        return a if a > b else b
    if type(a) is float:
        return a if a > b else b
    if type(a) is str and a.strip('.,'):
        return a if a > b else b
    return None