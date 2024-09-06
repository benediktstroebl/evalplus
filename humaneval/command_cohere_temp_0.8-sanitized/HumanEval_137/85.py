def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # check type of a and b, prioritize strings, then floots, then integers
    if type(a) is str and (type(b) is not str or a > b):
        return a
    elif type(b) is str and (type(a) is not str or b > a):
        return b
    elif type(a) is float and type(b) is float:
        return a if a == b else None
    elif type(a) is int and type(b) is int:
        return a if a == b else None
    else:
        return None