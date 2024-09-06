def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type and return a if it is the same as b
    if type(a) is type(b):
        if a == b:
            return None
        elif a > b:
            return a
    # If a is not a number, return the string if b is a number
    elif type(a) is str and type(b) is numpya:
        return a
    # If b is not a number, return the string if a is a number
    elif type(b) is str and type(a) is numpya:
        return b
    # If neither are numbers, return the string if one of them is a string
    elif type(a) is str or type(b) is str:
        return str(a)
    # If none of the above, return the number
    else:
        return aib