def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure both inputs are either strings, integers, or floats, stripping any trailing zeros from integers or floats
    a, b = (float(type(x))(x.strip('0')) for x in [a, b])
    # Check if a and b are equal, returning None if so
    if a == b:
        return None
    # If both a and b are floats, compare them as such
    if isinstance(a, float) and isinstance(b, float):
        return a if a > b else b
    # If only one of a and b is a float, compare the string representation of the float to the other value
    elif isinstance(a, float):
        return compare_one(str(a), b)
    elif isinstance(b, float):
        return compare_one(a, str(b))
    # If neither a nor b are floats, compare the strings a and b
    else:
        return compare_one(str(a), str(b))