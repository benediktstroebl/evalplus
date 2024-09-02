
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
    # Use type() to check the type of variable
    if type(a) == type(b):
        return cmp(a, b)
    elif type(a) == float and type(b) == str:
        # If a real number is represented as a string, the floating point might be . or ,
        # so use type() to check the type of variable
        if type(a) == str and type(b) == float:
            return cmp(float(a), float(b))
        elif type(a) == str and type(b) == int:
            # If the real number is represented as an integer, the string will be converted to an integer
            return cmp(float(a), b)
        else:
            return None
    elif type(a) == int and type(b) == str:
        return cmp(int(b), a)
    else:
        return None
