
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
    x = x == (y + z)
    if x == True:
        return any([isinstance(x, int), isinstance(y, int), isinstance(z, int)])
    else:
        return any([isinstance(x, float), isinstance(y, float), isinstance(z, float)])
    
