
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
    # if (type(a) == float or type(a) == int) and (type(b) == float or type(b) == int):
    #     return(max(a,b))
    # elif (type(a) == str and "," in a) or (type(b) == str and "," in b):
    #     if (type(a) == str and "," in a) and (type(b) == str and "," in b):
    #         a = float(a.replace(",", "."))
    #         b = float(b.replace(",", "."))
    #     elif type(a) == str and "," in a:
    #         a = float(a.replace(",", "."))
    #     elif type(b) == str and "," in b:
    #         b = float(b.replace(",", "."))
    #
    #     if a == b:
    #         return None
    #     elif a > b:
    #         return a
    #     else:
    #         return b
    #
    # if (type(a) == str and "." in a) or (type(b) == str and "." in b):
    #     if (type(a) == str and "." in a) and (type(b) == str and "." in b):
    #         a = float(a.replace(".", ""))
    #         b = float(b.replace(".", ""))
    #     elif type(a) == str and "." in a:
    #         a = float(a.replace(".", ""))
    #     elif type(b) == str and "." in b:
    #         b = float(b.replace(".", ""))
    #     if a == b:
    #         return None
    #     elif a > b:
    #         return a
    #     else:
    #         return b

    if type(a) == type(b):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == float and type(b) == int:
        a =
