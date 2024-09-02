
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
    # if type(a) != type(b):
    #     if type(a) == float or type(b) == float:
    #         return max(a, b)
    #     return None
    # if a > b:
    #     return a
    # if b > a:
    #     return b
    # return None

    # smaller = min(a,b)
    # larger = max(a,b)
    # if larger/smaller < 1:
    #     return larger
    # else:
    #     return None

    # if type(a) != type(b):
    #     if type(a) == float or type(b) == float:
    #         return max(a, b)
    #     return None
    # if a > b:
    #     return a
    # if b > a:
    #     return b
    # return None

    # Convert to strings and compare
    # If types are string, check for ',' or '.'
    # If types are float or int, convert to string
    a_str = a
    b_str = b
    if type(a) != type(b):
        if type(a) == float or type(b) == float:
            a_str = str(a)
            b_str = str(b)
        else:
            return None

    # If there are no ',' or '.', return max
    # If there is a ',' return the max of the part before the ','
    # If there is a '.', return the max of the part before the '.'
    if "," not in a_str and "," not in b_str:
        return max(a, b)
    if "," in a_str and "," in b_str:
        return max(a_str.split(",")[0], b_str.split(",")[0])
    if "," in a_str:
        return max(a_str.split(",")[0], b)
    if "," in b_str:
        return max(a, b_str.split(",")[0])
    if "." in a_str and "." in b_str:
