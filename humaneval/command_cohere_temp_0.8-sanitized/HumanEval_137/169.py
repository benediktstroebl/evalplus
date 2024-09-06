def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure both inputs are either strings, integers, or floats, stripping any trailing zeros from integers or floats
    a, b = (float(a.rstrip('0')) if isinstance(a, (str, int)) else a,
            float(b.rstrip('0')) if isinstance(b, (str, int)) else b)
    return max(a, b, key=lambda x: (isinstance(x, float), x)) if a != b else None