
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
    # Check the types
    if type(a) == type(b):
        if type(a) in [int, float]:
            return a > b
        elif type(a) in [str, type(b)]:
            if a.isdigit() and b.isdigit():
                return int(a) > int(b)
            elif a.find('.') < 0 and b.find('.') < 0:
                return int(a) > int(b)
            elif a.find('.') < 0:
                return int(b) > int(a)
            elif b.find('.') < 0:
                return int(a) > int(b)
        elif type(a) == str:
            return a.lower() > b.lower()
        else:
            return type(a) > type(b)
    elif type(a) is float and type(b) is int:
        return a > b
    elif type(a) is int and type(b) is float:
        return b > a
    else:
        return None
