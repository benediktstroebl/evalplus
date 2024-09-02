
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
    # casts to float if a float or int is given, if string, to float but keep as string
    if type(a) in (float, int) and type(b) in (float, int):
        a = float(a)
        b = float(b)
    elif type(a) in (str) and type(b) in (str):
        a = float(a.replace(',','.'))
        b = float(b.replace(',','.'))
    elif type(a) in (str) and type(b) in (float, int):
        a = float(a.replace(',','.'))
    elif type(b) in (str) and type(a) in (float, int):
        b = float(b.replace(',','.'))
    # compare
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None

