
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
    x1 = 0
    x2 = 0
    x3 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    z1 = 0
    z2 = 0
    z3 = 0
    if type(x) == int and type(y) == int and type(z) == int:
        x1 = x
        x2 = y
        x3 = z
        y1 = x + x2
        y2 = x + x3
        y3 = x + y1
        z1 = x + y2
        z2 = x + y3
        z3 = x + z1
    return x1 == y1 and x2 == y2 and x3 == y3 and x1
