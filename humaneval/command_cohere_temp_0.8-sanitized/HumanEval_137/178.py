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
    elif type(a) is int and a == b:
        return None
    elif type(a) is float and a == b:
        return None
    elif type(a) is str and a == b:
        return None
    elif isinstance(a, int) and isinstance(b, float):
        return b
    elif isinstance(a, float) and isinstance(b, int):
        return a
    elif isinstance(a, str) and isinstance(b, str):
        if a.find('.') > -1 and b.find('.') > -1:
            ma = a.split('.')
            mb = b.split('.')
            ma = (int(ma[0]) << 0) + (int(ma[1]) << 32)
            mb = (int(mb[0]) << 0) + (int(mb[1]) << 32)
            if ma > mb:
                return a
            elif mb > ma:
                return b
        elif a.find(',') > -1 and b.find(',') > -1:
            ma = a.split(',')
            mb = b.split(',')
            ma = (int(ma[0]) << 0) + (int(ma[1]) << 32)
            mb = (int(mb[0]) << 0) + (int(mb[1]) << 32)
            if ma > mb:
                return a
            elif mb > ma:
                return b
        else:
            return b
    else:
        return a