
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

    a = str(a)
    b = str(b)
    if "." in a and "," not in a:
        a = a.replace(",", ".")
    elif "." in a and "," in a:
        a = a.replace(",", "").replace(".", ",")
    if "." in b and "," not in b:
        b = b.replace(",", ".")
    elif "." in b and "," in b:
        b = b.replace(",", "").replace(".", ",")

    if a == b:
        return None
    elif float(a) > float(b):
        if type(a) == int:
            return int(a)
        elif type(a) == float:
            return float(a)
        elif type(a) == str:
            return str(a)
    elif float(a) < float(b):
        if type(b) == int:
            return int(b)
        elif type(b) == float:
            return float(b)
        elif type(b) == str:
            return str(b)


