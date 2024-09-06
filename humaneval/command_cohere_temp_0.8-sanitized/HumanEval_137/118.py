def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # check type of a and b, make sure they are the same or convert to float
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        elif a < b:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        # remove any commas or decimal points
        a = a.replace(",", "")
        b = b.replace(",", "")
        a = a.replace(".", "")
        b = b.replace(".", "")
        # if a and b are both integers, compare them, otherwise compare floats
        if a == b:
            return None
        elif a.isdigit() and b.isdigit():
            return int(a)
        elif a.replace(".", "") == b.replace(".", ""):
            return float(a)
        else:
            return float(a)
    else:
        return None