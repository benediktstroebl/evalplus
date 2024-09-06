def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if isinstance(a, str) and isinstance(b, str):
        compare = False
        if a == b:
            compare = True
        elif ('.' in a and ',' in b) or (',' in a and '.' in b):
            compare = False
        elif a.find('.') > b.find('.'):
            compare = a
        elif a.find('.') < b.find('.'):
            compare = b
        elif a.find(',') > b.find(','):
            compare = a
        elif a.find(',') < b.find(','):
            compare = b
        else:
            compare = False
        return compare
    elif isinstance(a, int) and isinstance(b, int):
        return a if a > b else b
    elif isinstance(a, float) and isinstance(b, float):
        return a if a > b else b
    elif isinstance(a, str) and isinstance(b, (int, float)):
        return a
    elif isinstance(a, (int, float)) and isinstance(b, str):
        return b
    else:
        return None