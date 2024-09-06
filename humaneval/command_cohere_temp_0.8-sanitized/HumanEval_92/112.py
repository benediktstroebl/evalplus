def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x == y + z or y == x + z or z == x + y and type(x) == int and type(y) == int and type(z) == int