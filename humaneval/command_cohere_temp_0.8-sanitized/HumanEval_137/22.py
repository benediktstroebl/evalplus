def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if isinstance(a, str) and isinstance(b, str):
        compare = len(max(a.replace('.', '').replace(',', ''), b.replace('.', '').replace(',', ''), key=len))
        return compare if compare != len(a) and compare != len(b) else None
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, (int, float)):
        return b
    elif isinstance(a, (int, float)) and isinstance(b, str):
        return a
    else:
        return None