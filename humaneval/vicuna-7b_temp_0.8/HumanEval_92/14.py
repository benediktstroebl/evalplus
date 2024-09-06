
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
    return any(abs(x-y) == abs(x-z) == abs(y-z) and x.is_integer() and y.is_integer() and z.is_integer() for x, y, z in [(x, y, z), (y, x, z), (x, z, y)] if x is not None else False