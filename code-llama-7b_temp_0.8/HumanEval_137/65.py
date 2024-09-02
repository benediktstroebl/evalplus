
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

    def is_float(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    if is_float(a) and is_float(b):
        if float(a) > float(b):
            return a
        elif float(a) < float(b):
            return b
        else:
            return None
    elif is_float(a):
        a = str(a)
        if a.find(".") > -1:
            a = a.replace(".",",")
        if float(a) > float(b):
            return a
        elif float(a) < float(b):
            return b
        else:
            return None
    elif is_float(b):
        b = str(b)
        if b.find(".") > -1:
            b = b.replace(".",",")
        if float(a) > float(b):
            return a
        elif float(a) < float(b):
            return b
        else:
            return None
    else:
        a = str(a)
        b = str(b)
        if a.find(".") > -1:
            a = a.replace(".",",")
        if b.find(".") > -1:
            b = b.replace(".",",")
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None

