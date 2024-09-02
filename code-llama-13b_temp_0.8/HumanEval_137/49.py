
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
    # Return None if the values are equal
    if a == b:
        return None

    # If a is greater
    if a > b:
        # If a is an integer
        if isinstance(a, int):
            # Return a in integer form
            return a
        # Else if a is a float
        elif isinstance(a, float):
            # Return a in float form
            return a
        # Else if a is a string
        else:
            # Return a in string form
            return a

    # Else if b is greater
    elif b > a:
        # If b is an integer
        if isinstance(b, int):
            # Return b in integer form
            return b
        # Else if b is a float
        elif isinstance(b, float):
            # Return b in float form
            return b
        # Else if b is a string
        else:
            # Return b in string form
            return b

