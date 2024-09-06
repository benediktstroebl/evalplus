def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y
    b = y + z
    c = x + z
    if a in [x, y, z] or b in [x, y, z] or c in [x, y, z]:
        return True
    elif type(x) is not int or type(y) is not int or type(z) is not int:
        return False
    else:
        return False