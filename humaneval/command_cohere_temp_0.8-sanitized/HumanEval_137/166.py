def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare = None
    if type(a) == type(b) and a != b:
        if type(a) == int:
            compare = a if a > b else b
        elif type(a) == float:
            compare = a if a > b else b
        # this condition covers str and other potential types that should be sorted alphabetically
        else:
            compare = a if a > b else b
    if compare == None:
        compare = None if a == b else b
    return compare