
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

    if not x or not y or not z:
        return False
    
    if isinstance(x, float) and isinstance(y, float) and isinstance(z, float):
        return False
    
    else:
        if x == (y + z) or y == (x + z) or z == (x + y):
            return True
        else:
            return False
        
    
    
    
    


















