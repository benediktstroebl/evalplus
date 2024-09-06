
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
    if type(x) is int and type(y) is int and type(z) is int:
        return any([x == y+z, y == x+z, z == x+y])
    else:
        return False

    # Alternative solution
    return x == y + z or y == x + z or z == x + y and all([type(x) is int, type(y) is int, type(z) is int])

