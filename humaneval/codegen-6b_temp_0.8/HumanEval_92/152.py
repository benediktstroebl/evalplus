
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
    a = x
    b = y
    c = z
    if type(a) == int or type(a) == float and int(a) == a:
        pass
    else:
        return False
    if type(b) == int or type(b) == float and int(b) == b:
        pass
    else:
        return False
