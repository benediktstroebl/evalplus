
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
    a_type = type(a)
    b_type = type(b)

    if a_type is int and b_type is int:
        if a > b:
            return a
        elif a == b:
            return None
        else:
            return b
    elif a_type is float and b_type is float:
        if a > b:
            return a
        elif a == b:
            return None
        else:
            return b
    elif a_type is str and b_type is str:
        if a.replace(".", ",").replace(",", ".") > b.replace(".", ",").replace(",", "."):
            return a
        elif a.replace(".", ",").replace(",", ".") == b.replace(".", ",").replace(",", "."):
            return None
        else:
            return b
    elif a_type is float and b_type is str:
        if float(a) > float(b.replace(".", ",").replace(",", ".")):
            return a
        elif float(a) == float(b.replace(".",
