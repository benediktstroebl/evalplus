
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
    # if a or b are strings and contain commas
    if type(a) == type(b) == str:
        if "," in a and "," in b:
            a = a.replace(",", ".")
            b = b.replace(",", ".")
            if float(a) == float(b):
                return None
            elif float(a) > float(b):
                return a
            else:
                return b
        # if a contains comma
        elif "," in a and "," not in b:
            a = a.replace(",", ".")
            if float(a) == float(b):
                return None
            elif float(a) > float(b):
                return a
            else:
                return b
        # if b contains comma
        elif "," not in a and "," in b:
            b = b.replace(",", ".")
            if float(a) == float(b):
                return None
            elif float(a) > float(b):
                return a
            else:
                return b
        # if none of them contain a comma
        else:
            if float(a) == float(b):
                return None
            elif float(a) > float(b):
                return a
            else:
                return b

    # if both are integers
    elif type(a) == type(b) == int:
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b

    # if one is integer and one is float
    elif type(a) != type(b):
        if isinstance(a, int):
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b
        elif isinstance(b, int):
            if a == b:
                return None
            elif a > b:
                return a
            else:
                return b

