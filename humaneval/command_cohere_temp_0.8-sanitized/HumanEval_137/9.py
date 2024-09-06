def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    # Check if a and b are both strings and compare those without converting
    if isinstance(a, str) and isinstance(b, str): 
        compare_result = max(a.strip(), b.strip())
    # If one value is a string, but not the other, convert the string to a float
    # and compare that way
    elif isinstance(a, str) or isinstance(b, str):
        a = float(a) if isinstance(a, str) else a
        b = float(b) if isinstance(b, str) else b
        compare_result = max(a, b)
    # Otherwise, they are both floats or ints, so compare normally
    else:
        compare_result = max(a, b)
    return compare_result if compare_result != a and compare_result != b else None