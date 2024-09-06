def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # check type of a and b, make sure they are the same or convert to str
    if type(a) != type(b):
        if isinstance(a, float) or isinstance(a, int):
            a, b = str(a), str(b)
        elif isinstance(b, float) or isinstance(b, int):
            a, b = str(a), str(b)
        else: 
            return None
    # check which is larger, return None if they are equal
    if a < b:
        return b
    elif a > b:
        return a
    else:
        return None