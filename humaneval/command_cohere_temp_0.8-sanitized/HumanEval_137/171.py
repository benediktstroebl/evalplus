def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        return 'ERROR: The arguments must be of the same type!'
    # Check integer
    if type(a) is int and a >= b:
        return a
    # Check float
    if type(a) is float and a >= b:
        return a
    # Check string
    if type(a) is str and a >= b:
        return a
    return None