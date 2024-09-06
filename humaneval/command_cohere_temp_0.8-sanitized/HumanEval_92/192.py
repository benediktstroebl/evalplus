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
    elif a == b and a == c:
        return False
    else:
        return any([type(i) for i in [x, y, z]]) == int and any_int(a, b, c)