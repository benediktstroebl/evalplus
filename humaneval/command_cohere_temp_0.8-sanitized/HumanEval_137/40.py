def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # check type of a and b, needed for python 3.7 and higher
    if type(a) is not type(b):
        return None
    # both are strings: compare lexically, assuming strings are converted correctly
    if type(a) is str:
        return a if a > b else b
    # both are numbers: compare numerically
    return max(a, b)