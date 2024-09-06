def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type of a and b, needed to resolve potential IEEE 754 NaN confusion
    if isinstance(a, str) and isinstance(b, str):
        if a == b:
            return None
        elif a < b:
            return a
        else:
            return b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, str) and isinstance(b, (int, float)):
        if a == b:
            return None
        elif float(a) > b:
            return a
        else:
            return b
    elif isinstance(a, (int, float)) and isinstance(b, str):
        if a == b:
            return None
        elif a > float(b):
            return a
        else:
            return b
    else:
        assert False, ("Unhandled combination of variable types: "
                       f"a={type(a)}, b={type(b)}")