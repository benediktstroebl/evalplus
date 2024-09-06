def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if isinstance(a, str) and isinstance(b, str):
        compare = lambda x, y: x if x == y else y
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        compare = lambda x, y: x if x > y else y
    elif isinstance(a, str) or isinstance(b, str):
        compare = lambda x, y: x if x > y else y
    else:
        compare = lambda x, y: None
    return compare(a, b)