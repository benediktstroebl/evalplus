def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if isinstance(a, str) and isinstance(b, str):
        compare = False
        for char in a:
            if char not in ['', '.', ',']:
                compare = False
                break
            if b < a:
                return a
            elif b > a:
                return b
        if not compare:
            return a
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(a, b)
    elif isinstance(a, str) or isinstance(b, str):
        if a == b:
            return None
        elif (isinstance(a, str) and isinstance(b, int)) or (isinstance(b, str) and isinstance(a, int)):
            return a if isinstance(a, str) else b
        elif (isinstance(a, str) and isinstance(b, float)) or (isinstance(b, str) and isinstance(a, float)):
            return a if isinstance(a, str) else b
    else:
        return max(a, b)