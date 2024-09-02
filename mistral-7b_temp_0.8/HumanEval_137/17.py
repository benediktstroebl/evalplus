
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

    """
    if float(a) > float(b):
        return float(a)
    elif float(a) < float(b):
        return float(b)
    else:
        return None
    """
    if isinstance(a, str) and isinstance(b, str):
        if a.split(',')[0] > b.split(',')[0]:
            return a
        elif a.split(',')[0] < b.split(',')[0]:
            return b
        else:
            return None
    if isinstance(a, str) and isinstance(b, float):
        if a.split(',')[0] > float(b):
            return a
        elif a.split(',')[0] < float(b):
            return b
        else:
            return None
    if isinstance(a, float) and isinstance(b, str):
        if float(a) > float(b.split(',')[0]):
            return a
        elif float(a) < float(b.split(',')[0]):
           
