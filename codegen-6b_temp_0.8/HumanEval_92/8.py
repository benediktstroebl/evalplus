
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
    if float(x + y + z) == float(x) or float(x + y + z) == float(y) or float(x + y + z) == float(z) or float(x + y + z) == float(x + y) or float(x + y + z) == float(x + z) or float(x + y + z) == float(y + z) or (float(x + y + z) - int(float(x + y + z))) > 0 or (float(x + y + z) - int(float(x + y + z))) < 0:
        return True
    return False
    


