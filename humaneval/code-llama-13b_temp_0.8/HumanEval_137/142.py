
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
    # def convert(num):
    #     if isinstance(num, str):
    #         return float(num.replace(",", "."))
    #     else:
    #         return num

    if a == b:
        return None

    if a > b:
        if isinstance(a, str):
            return a.replace(".", ",")
        else:
            return a
    else:
        if isinstance(b, str):
            return b.replace(".", ",")
        else:
            return b

    # return convert(a) if convert(a) > convert(b) else convert(b) if convert(b) > convert(a) else None

