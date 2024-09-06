
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

    if a == b:
        return None
    if type(a) == float or type(a) == int:
        if a > b:
            return a
        else:
            return b
    if type(a) == str:
        a = a.replace(",", ".")
        if a[-1] == ".":
            a = a[:-1]
        if b[-1] == ".":
            b = b[:-1]
        if a.isnumeric() and b.isnumeric():
            a = int(a)
            b = int(b)
            return compare_one(a, b)
        elif a.isnumeric() == False and b.isnumeric() == False:
            a = float(a)
            b = float(b)
            return compare_one(a, b)
        else:
            return a
    return "Please enter numbers only."
