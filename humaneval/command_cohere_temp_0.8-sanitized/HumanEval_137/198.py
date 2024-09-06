def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare = None
    if type(a) == type(b) and type(a) in [int, float, str]:
        if a == b:
            compare = None
        elif type(a) == str:
            if a.find(',') > b.find(',') or (a.find('.') > b.find('.')):
                compare = a
            elif b.find(',') > a.find(',') or (b.find('.') > a.find('.')):
                compare = b
        else:
            if a > b:
                compare = a
            else:
                compare = b
    return compare