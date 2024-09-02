
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
    if type(a) != type(b):
        return type(a) == str and a.find(".") != -1 and a.find(",") != -1 and \
            b.find(".") != -1 and b.find(",") != -1 or \
            type(a) == float and a != b else \
            type(a) == int and int(a) > int(b) else \
            type(b) == int and int(b) > int(a)
    elif type(a) == float and float(a) > float(b):
        return a
    elif type(a) == int and int(a) > int(b):
        return a
    elif type(b) == float and float(b) > float(a):
        return b
    elif type(b) == int and int(b) > int(a):
        return b
    else:
        return None
