
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
    elif isinstance(a, float) or isinstance(b, float):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif a == str(b):
        if a > str(b):
            return str(a)
        elif str(a) < str(b):
            return str(b)
        else:
            return None
    else:
        raise ValueError("Invalid type of input")

a_list = [1, 2.5, "2,3", "5,1", 1, 5.2, "1", "2,3", "3", 5.5, 6, "6"]
b_list = [1, 2.5, "2,3", "5,1", 1, 5.2, "1", "2,3", "3", 5.5, 6, "6"]

for a, b in zip(a_list, b_list):
    print(compare_one(a, b))