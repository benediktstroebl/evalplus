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
    if type(a) is not type(b):
        return None
    elif type(a) is str and type(b) is str and a == b:
        return None
    elif type(a) is int and type(b) is int:
        return max(a, b)
    elif type(a) is float and type(b) is float:
        return max(a, b)
    elif type(a) is str and type(b) is float:
        if a.find('.') != -1 and a.find(',') != -1:
            return b
        elif a.find('.') != -1:
            temp = a.replace(',', '.')
            return temp
        elif a.find(',') != -1:
            temp = a.replace('.', ',')
            return temp
        else:
            return b
    elif type(a) is float and type(b) is str:
        if b.find('.') != -1 and b.find(',') != -1:
            return a
        elif b.find('.') != -1:
            temp = b.replace(',', '.')
            return a
        elif b.find(',') != -1:
            temp = b.replace('.', ',')
            return a
        else:
            return a
    elif type(a) is str and type(b) is int:
        return a
    elif type(a) is str and type(b) is float:
        return a
    elif type(a) is float and type(b) is int:
        return a