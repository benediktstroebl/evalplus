def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    # Check if a and b are both strings first
    if type(a) is str and type(b) is str:
        compare_result = max(a.replace(',', ''), b.replace(',', ''))
    # If one of them is a string, then the other one must be a number
    elif type(a) is str or type(b) is str:
        # If a is string, return b if it's a number
        if type(a) is str:
            compare_result = b
        # If b is string, return a if it's a number
        else:
            compare_result = a
    # If neither are strings, then they are both numbers
    else:
        compare_result = max(a, b)
    # If the values are equal, return None
    if compare_result == None:
        compare_result = None
    return compare_result