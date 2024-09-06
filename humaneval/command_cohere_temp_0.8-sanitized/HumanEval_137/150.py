def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_val = None
    # Check if the variables are of the same type
    if type(a) == type(b):
        # If types are the same, check their values.
        if a > b:
            compare_val = a
        elif a < b:
            compare_val = b
    # If types are different, check which variable is of type string, and that variable is the larger one.
    elif type(a) == str() and type(b) != str():
        compare_val = a
    elif type(a) != str() and type(b) == str():
        compare_val = b
    return compare_val