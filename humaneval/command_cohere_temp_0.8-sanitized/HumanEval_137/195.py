def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure both inputs are either strings, integers, or floats
    a = float(a) if isinstance(a, str) else a
    b = float(b) if isinstance(b, str) else b

    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None