def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        return None
    # Check values
    if a == b:
        return None
    # Check string values
    if type(a) is str and type(b) is str:
        if a.find('.') > b.find('.'):
            return a
        elif a.find('.') < b.find('.'):
            return b
        elif a.find(',') > b.find(','):
            return a
        elif a.find(',') < b.find(','):
            return b
    # Check number values
    if type(a) is int and type(b) is int:
        return max(a, b)
    elif type(a) is float and type(b) is float:
        return max(a, b)
    elif type(a) is int and type(b) is float:
        return b
    elif type(a) is float and type(b) is int:
        return a
    else:
        return None