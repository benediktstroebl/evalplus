
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
    # I did not know about math.isnan, so I did this:
    if a != a: a = 0
    if b != b: b = 0

    if type(a) == float or type(b) == float:
        if float(a) > float(b):
            return float(a)
        elif float(b) > float(a):
            return float(b)
        else:
            return None
    elif type(a) == int or type(b) == int:
        if int(a) > int(b):
            return int(a)
        elif int(b) > int(a):
            return int(b)
        else:
            return None
    elif type(a) == str or type(b) == str:
        if float(a.replace(',','.')) > float(b.replace(',','.')):
            return float(a.replace(',','.'))
        elif float(b.replace(',','.')) > float(a.replace(',','.')):
            return float(b.replace(',','.'))
        else:
            return None




