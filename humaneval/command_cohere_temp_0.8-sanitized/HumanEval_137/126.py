def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        return None
    # Convert string values to float to compare
    a = float(a) if type(a) is str else a
    b = float(b) if type(b) is str else b
    # Compare values and return the larger one
    if a > b:
        return a
    return b