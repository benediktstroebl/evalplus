def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # check type of a and b, make sure they are the same
    if type(a) is not type(b):
        return 'Error: Inputs should be of the same type!'
    # both strings
    if type(a) is str:
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    # both integers
    if type(a) is int:
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    # one string, one integer
    if type(a) is str and type(b) is int:
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    # one integer, one string
    if type(a) is int and type(b) is str:
        if a == b:
            return None
        elif a > b:
            return b
        else:
            return a
    # both floating numbers
    if type(a) is float and type(b) is float:
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
        return 'Error: Unexpected types!'