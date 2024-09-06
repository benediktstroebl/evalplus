
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

    # If input is string and both input contain "." then return None
    if type(a) == str and type(b) == str:
        if a.find(".") != -1 and b.find(".") != -1:
            return None

    # if both are integers then return max(a,b)
    elif type(a) == int and type(b) == int:
        return max(a,b)

    # if both are floats then return max(a,b)
    elif type(a) == float and type(b) == float:
        return max(a,b)

    # if both are strings then return max(a,b)
    elif type(a) == str and type(b) == str:
        return max(a,b)

    # if any one is string then return that string
    elif type(a) == str and type(b) != str:
        return a
    elif type(a) != str and type(b) == str:
        return b
