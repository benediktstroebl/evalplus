def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare = None
    if type(a) == type(b):
        if isinstance(a, int) or isinstance(a, float):
            compare = a if a > b else b
        elif isinstance(a, str):
            la = len(a)
            lb = len(b)
            ca = a.count('.')
            cb = b.count('.')
            if la == lb and ca == cb:
                compare = a if a > b else b
            elif la > lb and ca == 0 and cb == 0:
                compare = a
            elif lb > la and cb == 0 and ca == 0:
                compare = b
            elif la == lb and ca == 1 and cb == 1:
                compare = a if a > b else b
            elif la == lb and ca == 0 and cb == 1:
                compare = b
            else:
                compare = a if a > b else b
        elif isinstance(a, bool) or isinstance(a, NoneType):
            compare = a if a != b else None
        else:
            compare = a if a > b else b
    return compare