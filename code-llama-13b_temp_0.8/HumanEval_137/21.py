
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
    #if type(a) == str and type(b) == int:
    #    if float(a.replace(',', '.')) < b:
    #        return b
    #    else:
    #        return a
    #elif type(a) == int and type(b) == str:
    #    if b.replace(',', '.') < a:
    #        return a
    #    else:
    #        return b
    #elif type(a) == str and type(b) == str:
    #    if float(a.replace(',', '.')) < float(b.replace(',', '.')):
    #        return b
    #    else:
    #        return a
    #elif type(a) == int and type(b) == int:
    #    if a < b:
    #        return b
    #    else:
    #        return a
    #elif type(a) == float and type(b) == float:
    #    if a < b:
    #        return b
    #    else:
    #        return a
    #elif type(a) == float and type(b) == int:
    #    if a < b:
    #        return b
    #    else:
    #        return a
    #elif type(a) == int and type(b) == float:
    #    if a < b:
    #        return b
    #    else:
    #        return a
    #elif a == b:
    #    return None
    
    return max(a, b, key=lambda x: float(str(x).replace(',', '.'))) if type(a) == str or type(b) == str else max(a, b) if a < b else min(a, b)

