
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """

    # a and b are floats
    if type(a) == float and type(b) == float:
        return a if a > b else b if a < b else None

    # a or b is an int
    if type(a) == int or type(b) == int:
        return a if a > b else b if a < b else None

    # a and b are strings
    if type(a) == str and type(b) == str:
        return a if a > b else b if a < b else None

    return None

