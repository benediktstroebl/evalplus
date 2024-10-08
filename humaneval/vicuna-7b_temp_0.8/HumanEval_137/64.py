
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
    if type(a) == type(b):
        if a > b:
            return a
        else:
            return b
    elif type(a) == type(float):
        if a > b:
            return a
        else:
            return b
    elif type(a) == type(str):
        if a.isnumeric() and b.isnumeric():
            if a.isdigit() and b.isdigit():
                if int(a) > int(b):
                    return int(a)
                else:
                    return int(b)
            else:
                return str(a)
        else:
            return b
    else:
        return None

compare_one(10, 2.5)  # 2.5
compare_one(1, "2,3")  # "2,3"
compare_one("5,1", "6")  # "6"
compare_one("1", 1)  # None
