
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

    try:
        if int(x) + int(y) == int(z): return True
        if int(y) + int(z) == int(x): return True
        if int(z) + int(x) == int(y): return True
    except:
        return False
        
    
    return False
