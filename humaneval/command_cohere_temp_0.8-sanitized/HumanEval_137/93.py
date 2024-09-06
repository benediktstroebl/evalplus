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
    # both are strings: compare plain values, needed for python 3.7 and higher
    if type(a) is str and type(b) is str:
        return a if a > b else b
    # one of them is string: S. Thumm, needed for python 3.7 and higher
    if type(a) is str or type(b) is str:
        return None
    # both are numbers: compare plain values
    if a > b:
        return a
    return b