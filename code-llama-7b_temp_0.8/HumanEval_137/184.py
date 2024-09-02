
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
    
    if str(a) == str(b):
        return None
    elif type(a) == type(b):
        return max(a, b)
    else:
        if type(a) == float or type(b) == float:
            a = float(a)
            b = float(b)
            return max(a, b)
        elif type(a) == int or type(b) == int:
            a = int(a)
            b = int(b)
            return max(a, b)

