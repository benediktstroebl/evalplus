
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
        else:
            return b
    elif type(a) == str and type(b) == float:
        if float(a) > float(b):
            return float(a)
        else:
            return float(b)
    elif type(b) == str and type(a) == float:
        if float(b) > float(a):
            return float(b)
        else:
            return float(a)
    elif type(a) == int and type(b) == str:
        if int(b) > int(a):
            return int(b)
        else:
            return int(a)
    elif type(b) == int and type(a) == str:
        if int(a) > int(b):
            return int(a)
        else:
            return int(b)
    else:
        return None

for a, b in zip(comparison_list, comparison_list[1:]):
    print(compare_one(a, b), end="\t")
