def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure both inputs are either strings, integers, or floats
    a, b = str(a), str(b)
    # Check if the values are equal
    if a == b:
        return None
    # Check if one of the values is a string, and if so, ensure the string is the largest value
    if isinstance(a, str) and (isinstance(b, int) or isinstance(b, float)):
        return a
    # At this point, a is either an integer or a float, so we return b (which is also an integer or float)
    return b