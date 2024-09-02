
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
    
    if (int(x) + int(y) == int(z)) and (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return True
    elif (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)) or (isinstance(x, int) and isinstance(y, int) and not isinstance(z, int)) or (isinstance(x, int) and not isinstance(y, int) and isinstance(z, int)) or (not isinstance(x, int) and isinstance(y, int) and isinstance(z, int)) or (not isinstance(x, int) and not isinstance(y, int) and isinstance(z, int)) or (not isinstance(x, int) and isinstance(y, int) and not isinstance(z, int)) or (isinstance(x, int) and not isinstance(y, int) and not isinstance(z, int)) or (not isinstance(x, int) and isinstance(y, int) and not isinstance(z, int)) or (not isinstance(x, int) and not isinstance(y, int) and not isinstance(z, int)):
        return False
        
    elif (isinstance(x, int) and isinstance(y, int) and isinstance(z, float)) or (isinstance(x, int) and isinstance(z, int) and isinstance(y, float)) or (isinstance(y, int) and isinstance(z, int) and isinstance(x, float)) or (isinstance(x, float) and isinstance(y, int) and isinstance(z, int)) or (isinstance(y, float) and isinstance(z, int) and isinstance(x, int)) or (isinstance(z, float) and isinstance(x, int) and isinstance(y, int)) or (isinstance(x, float) and isinstance(y, float) and isinstance(z, int)) or (isinstance(y, float) and isinstance(x, float) and isinstance(z, int)) or (isinstance(z, float) and isinstance(y,
