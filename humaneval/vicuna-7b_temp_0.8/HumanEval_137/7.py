
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
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, string) or isinstance(b, string):
        if a.isdigit() and b.isdigit():
            return float(a) > float(b)
        elif a.find('.') < b.find('.') or (a.find(',') < b.find(',') and a.find('-') < b.find('-')):
            return float(a) > float(b)
        elif a.find(',') < b.find(',') and a.find('-') < b.find('-'):
            return float(b) > float(a)
        else:
            return b.compare(a)
    elif isinstance(a, float) or isinstance(b, float):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    else:
        return b.compare(a)
