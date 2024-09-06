def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure both inputs are either strings, integers, or floats, then compare their values
    typeof_a = type(a)
    typeof_b = type(b)
    if typeof_a == typeof_b:
        if a == b:
            return None
        elif a > b:
            return a
    elif typeof_a in [int, float] and typeof_b in [str,]:
        return b
    elif typeof_a in [str,] and typeof_b in [int, float]:
        return a
    else:
        raise ValueError("Input variables must be of the same type or string, integer, or float.")