def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_one.equal = False
    if type(a) is not type(b):
        if isinstance(a, str) and isinstance(b, str):
            if a.find('.') > b.find('.') or (a.find('.') == b.find('.') and a.find(',') < b.find(',')):
                return a
            else:
                return b
        elif isinstance(a, float) or isinstance(a, int):
            return a
        elif isinstance(b, (float, int)):
            return b
        elif isinstance(a, str) or isinstance(b, str):
            compare_one.equal = True
    elif a == b:
        compare_one.equal = True
    return None