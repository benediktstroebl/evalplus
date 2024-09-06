
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
    if x==y+z:
        return True
    if x==y:
        return False
    if x==z or z==y:
        return False
    if x>0 and y>0 and z>0 and x+y+z==0 and isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return True
    else:
        return False
