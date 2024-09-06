
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
    
    a=x+y
    b=y+z
    c=x+z
    
    
    return ((a==a.__trunc__()) and (a==a.__round__()) and b==b.__trunc__() and b==b.__round__() and c==c.__trunc__() and c==c.__round__())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
