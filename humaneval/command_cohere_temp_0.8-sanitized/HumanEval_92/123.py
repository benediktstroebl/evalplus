def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y
    b = x + z
    c = y + z
    return ((type(x) == int) and (type(y) == int) and (type(z) == int) and 
            (a in [x, y, z]) or 
            (b in [x, y, z]) or 
            (c in [x, y, z]))