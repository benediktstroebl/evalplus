def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y
    b = x + z
    c = y + z

    if not isinstance(x) or not isinstance(y) or not isinstance(z):
        return False
    
    if a in (b, c) and a == int(a):
        return True
    elif b in (a, c) and b == int(b):
        return True
    elif c in (a, b) and c == int(c):
        return True
    else:
        return False