def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure both inputs are either strings, integers, or floats, then convert to floats
    try:
        a, b = float(a), float(b)
        # Returns True if inputs are equal, otherwise False
        return a if a > b else b if b > a else None
    except ValueError:
        # If the inputs are not numeric, they must be strings
        return max(a, b, key=len)