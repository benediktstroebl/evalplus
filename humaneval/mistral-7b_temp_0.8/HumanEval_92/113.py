
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
    a = x + y
    b = y + z
    c = x + z
    if a == x or b == y or c == z:
        if a == x and a == int(a) and a == round(a) and a == float(a):
            if b == y and b == int(b) and b == round(b) and b == float(b):
                if c == z and c == int(c) and c == round(c) and c == float(c):
                    return True


    return False


    '''
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False
    
    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''







    '''
    Examples
    any_int(5, 2, 7
