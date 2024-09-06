def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure both inputs are either strings, integers, or floats
    a = str(a) if type(a) != str else a
    b = str(b) if type(b) != str else b

    # Check if a and b are equal
    if a == b:
        return None
    # If a is the largest value, return a
    elif a > b:
        return a
    # If b is the largest value, return b
    else:
        return b