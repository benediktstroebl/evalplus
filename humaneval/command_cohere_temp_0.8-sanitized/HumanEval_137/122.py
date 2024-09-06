def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        if isinstance(a, float) or isinstance(a, int):
            return a
        elif isinstance(b, float) or isinstance(b, int):
            return b
        elif isinstance(a, str) and isinstance(b, str):
            # Convert string to float and compare
            float_a = float(a)
            float_b = float(b)
            if float_a == float_b:
                return None
            elif float_a > float_b:
                return a
            else:
                return b
        else:
            return str(a)
    else:
        # Value comparison for integers, floats, or strings
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b