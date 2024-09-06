def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure a and b are either both strings or both numbers
    a, b = str(a), str(b) if isinstance(a, str) and isinstance(b, str) else (a, b)
    
    # Check which variable is larger
    return a if a > b else b if b > a else None