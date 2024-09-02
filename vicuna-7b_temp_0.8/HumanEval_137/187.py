
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
    if isinstance(a, numbers.Number):
        if isinstance(b, numbers.Number):
            if a.is_integer():
                if b.is_integer():
                    return b if b > a else a
                else:
                    return a if a > b else b
            elif a.is_float():
                if b.is_float():
                    if a > b:
                        return a
                    elif b > a:
                        return b
                else:
                    return a
            else:
                return a if a > b else b
        elif b.is_integer():
            return b if b > a else a
        elif b.is_float():
            if a > b:
                return a
            elif b > a:
                return b
        else:
            return a if a > b else b
    elif isinstance(a, str):
        if isinstance(b, str):
            if a.isdigit():
                if b.isdigit():
                    return b if b > a else a
                else:
                    return a if a > b else b
            else:
                return a if a > b else b
        elif b.isdigit():
            if a.isdigit():
                if a > b:
                    return a
                elif b > a:
                    return b
                else:
                    return None
            else:
                return a if a > b else b
    else:
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
