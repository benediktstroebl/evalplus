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
    if type(a) is not type(b):
        # If the types are different, return the larger value with its original type
        if type(a) is int and type(b) is float:
            return b
        elif type(a) is float and type(b) is int:
            return a
        elif type(a) is str and type(b) is int:
            return str(b)
        elif type(a) is int and type(b) is str:
            return str(a)
        elif type(a) is str and type(b) is float:
            return b
        elif type(a) is float and type(b) is str:
            return a
        else:
            return None
    elif a == b:
        return None
    else:
        return max(a, b)