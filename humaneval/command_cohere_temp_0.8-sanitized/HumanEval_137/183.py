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
        # check if it is a string that represents a number
        if a.replace('.', '', 1).replace(',', '', 1).isdigit() and b.replace('.', '', 1).replace(',', '', 1).isdigit():
            if float(a) > float(b):
                return a
            elif float(a) < float(b):
                return b
        else:
            if len(a) > len(b):
                return a
            elif len(a) < len(b):
                return b
    return None