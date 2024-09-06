
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
    if type(x) is not int:
        x = float(x)
    if type(y) is not int:
        y = float(y)
    if type(z) is not int:
        z = float(z)
    if x<=0 or y<=0 or z<=0:
        return False
    if x+y == z and (type(x) is int and type(y) is int and type(z) is int):
        return True
    return False
    
































































































































