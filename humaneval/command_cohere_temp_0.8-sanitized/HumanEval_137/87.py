def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # check type of a and b, make sure they are either int, float, or str
    assert isinstance(a, (int, float, str)), "Both inputs must be int, float, or str."
    assert isinstance(b, (int, float, str)), "Both inputs must be int, float, or str."
    # checks if a is equal to b
    if a == b:
        return None
    # checks if a and b are int
    elif isinstance(a, int) and isinstance(b, int):
        return a if a > b else b
    # checks if a is float and b is int, float, or str
    elif isinstance(a, float) and (isinstance(b, (int, float, str))):
        return a if a > b else b
    # checks if a is str and b is int, float, or str
    elif isinstance(a, str) and (isinstance(b, (int, float, str))):
        return a if a > b else b