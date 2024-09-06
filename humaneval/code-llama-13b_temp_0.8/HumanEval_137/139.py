
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
    # Converting "1" type to float and checking the bigger one
    if type(a) is str and type(b) is int:
        a = float(a.replace(',','.'))
    elif type(a) is int and type(b) is str:
        b = float(b.replace(',','.'))
    # Converting "1.0" type to float and checking the bigger one
    elif type(a) is str and type(b) is float:
        a = float(a.replace(',','.'))
    elif type(a) is float and type(b) is str:
        b = float(b.replace(',','.'))
    # Converting "1" type to integer and checking the bigger one
    elif type(a) is float and type(b) is int:
        a = int(a)
    elif type(a) is int and type(b) is float:
        b = int(b)

    # Comparing the 2 numbers
    if a > b:
        return a
    elif a == b:
        return None
    else:
        return b

