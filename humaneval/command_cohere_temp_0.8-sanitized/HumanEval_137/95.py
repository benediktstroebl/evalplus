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
        b = float(b) if b != "" else 0
    except ValueError:
        a = 0 if a == "" else a
        b = 0 if b == "" else b

    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None