
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
    elif type(a) == str and type(b) == float:
        if a.isdigit() == False and b.isdigit() == False:
            if a.isalpha() == True:
                return b
            else:
                return a
        elif a.isdigit() == True and b.isdigit() == True:
            if a.isalpha() == True:
                return b
            else:
                return a
    elif type(b) == str and type(a) == float:
        if a.isdigit() == False and b.isdigit() == False:
            if b.isalpha() == True:
                return a
            else:
                return b
        elif a.isdigit() == True and b.isdigit() == True:
            if a.isalpha() == True:
                return b
            else:
                return a
    else:
        raise ValueError("Invalid input")
