
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

    # if a and b are not of the same type, return the type of a that is greater
    # if a and b are of the same type, return None if they are equal, else the greater

    if type(a) != type(b):
        return a if type(a) == float and a > b else b if type(b) == float and b > a else type(a)(a) if a > b else type(b)(b)
    elif a == b:
        return None
    else:
        return a if a > b else b

