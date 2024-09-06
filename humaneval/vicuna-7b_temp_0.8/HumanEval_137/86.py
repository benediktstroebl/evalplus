
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
        return cmp(a, b)
    elif type(a) == type(str) and type(b) == type(str):
        if a.isdigit() != b.isdigit():
            return cmp(a, b)
        elif a.isdigit() == b.isdigit():
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1
            else:
                return 0
    elif type(a) == type(float) and type(b) == type(float):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0
    elif type(a) == type(int) and type(b) == type(int):
        return cmp(a, b)
    else:
        return None
