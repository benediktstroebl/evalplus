
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
        return "Please provide integers or real numbers as strings"
    elif type(a) == str:
        if "," in a and "," in b:
            a = float(a.replace(",", "."))
            b = float(b.replace(",", "."))
        elif "." in a and "." in b:
            a = float(a)
            b = float(b)
        else:
            a = float(a)
            b = float(b)
    elif type(a) != int and type(b) != int:
        a = float(a)
        b = float(b)
    elif type(a) == int and type(b) == int:
        pass
    else:
        return "Please provide integers or real numbers as strings"

    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b

