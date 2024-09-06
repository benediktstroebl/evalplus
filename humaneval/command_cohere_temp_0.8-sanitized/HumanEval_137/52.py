def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure a and b are either both strings or both numbers
    try:
        a = float(a)
        b = float(b) if b else 0
    except:
        pass
    else:
        return max(a, b)
    # If types are different, convert to string and compare that way
    if type(a) != type(b):
        return max(str(a), str(b))
    # If values are equal, return None
    return None