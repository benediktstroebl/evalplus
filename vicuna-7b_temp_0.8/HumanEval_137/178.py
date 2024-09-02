
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
        elif a < b:
            return b
    elif type(a) == type(float):
        if a > float(b):
            return float(a)
        elif a < float(b):
            return float(b)
    elif type(a) == str and type(b) == str:
        if a.isnumeric() and b.isnumeric():
            if a > b:
                return float(a)
            elif a < b:
                return float(b)
        else:
            if a.strip(".").isalpha() and b.strip(".").isalpha():
                if a.strip(".").strip(" ") > b.strip("."):
                    return float(a)
                elif b.strip(".").strip(" ") > a.strip("."):
                    return float(b)
        return None
    else:
        return None

compare_one(1, 2.5)
compare_one(1, "2,3")
compare_one("5,1", "6")
compare_one("1", 1)