
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

    # convert to float and return max
    if type(a) == type(b):
        if type(a) == float or type(a) == int:
            return a if a > b else b
    if type(a) == str or type(b) == str:
        x = float(a) if a.replace(".", "", 1).isdigit() else a
        y = float(b) if b.replace(".", "", 1).isdigit() else b
        if type(x) == float and type(y) == float:
            return y if y > x else x
        else:
            return x if x > y else y
    return None

