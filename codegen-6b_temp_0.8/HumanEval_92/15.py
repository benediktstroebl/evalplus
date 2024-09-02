
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
    if all(isinstance(i, int) for i in (x,y,z)) and x+y<z:
        return True
    return False
    
    ##my test:

    if all(isinstance(i, int) for i in (x,y,z)) and x+y<z and type(x)==int and type(y)==int and type(z)==int:
        return True
    return False
    
    # another doesn't work
    if all(isinstance(i, (int, float)) for i in (x, y, z)):
        return (x*x)+(y*y)<z*z
    else:
        return False
    # given solution
    #return any([(x>=y+z and  x-y<z and isinstance(x, int) and isinstance(y, int) and isinstance(z, int)),
    #            (y>=x+z and  y-x<z and isinstance(y, int) and isinstance(x, int) and isinstance(z, int)),
    #            (z>=x+y and  z-x<y and isinstance(z, int) and isinstance(x, int) and isinstance(y, int))])

