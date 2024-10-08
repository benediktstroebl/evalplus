
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
    if type(a) == type(b):
        return None
    if (type(a) == float or type(a) == int) and (type(b) == float or type(b) == int):
        return max(a,b)
    if (type(a) == str and ',' in a) or (type(b) == str and ',' in b):
        a = a.replace(',','.')
        b = b.replace(',','.')
        if float(a) > float(b):
            return float(a)
        elif float(a) < float(b):
            return float(b)
        else:
            return None
    elif (type(a) == str and '.' in a) or (type(b) == str and '.' in b):
        if float(a.replace('.','')) > float(b.replace('.',''))):
            return float(a.replace('.',''))
        elif float(a.replace('.','')) < float(b.replace('.',''))):
            return float(b.replace('.',''))
        else:
            return None
    else:
        if float(a) > float(b):
            return float(a)
        elif float(a) < float(b):
            return float(b)
        else:
            return None

