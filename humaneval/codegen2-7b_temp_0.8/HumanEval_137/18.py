
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
    if type(a) is type(b):
        return a
    else:
        if type(a) is str:
            a = list(a.split(','))
            a = [float(i) for i in a]
        if type(b) is str:
            b = list(b.split(','))
            b = [float(i) for i in b]
        if type(a) == list and type(b) == list:
            return [x if y == x else y for y in b for x in a]
        if type(a) == list:
            return a
        if type(b) == list:
            return
