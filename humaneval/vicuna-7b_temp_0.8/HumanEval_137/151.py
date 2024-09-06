
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
    if isinstance(a, float) or isinstance(a, int) or isinstance(a, str):
        if isinstance(b, float) or isinstance(b, int) or isinstance(b, str):
            if type(a) == type(b):
                return cmp(a, b)
            elif type(a) == type(b):
                if a > b:
                    return 1
                elif a < b:
                    return -1
                else:
                    return 0
        elif isinstance(b, string):
            if type(a) == type(b):
                return cmp(float(a), float(b))
            elif float(a) > float(b):
                return 1
            elif float(a) < float(b):
                return -1
            else:
                return 0
    elif isinstance(b, float) or isinstance(b, int) or isinstance(b, str):
        if isinstance(a, float) or isinstance(a, int) or isinstance(a, str):
            if isinstance(b, float) or isinstance(b, int) or isinstance(b, str):
                if type(a) == type(b):
                    return cmp(a, b)
                elif type(a) == type(b):
                    if a > b:
                        return 1
                    elif a < b:
                        return -1
                    else:
                        return 0
                elif type(a) == type(float(b)):
                    if a > float(b):
                        return 1
                    elif a < float(b):
                        return -1
                    else:
                        return 0
                elif isinstance(a, str) and isinstance(b, str):
                    if type(a) == type(b):
                        return cmp(float(a), float(b))
                    elif float(a) > float(b):
                        return 1
                    elif float(a) < float(b):
                        return -1
                    else:
                        return 0
            else:
                return None
