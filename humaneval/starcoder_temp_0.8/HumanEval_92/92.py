
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
    # Your code here
    if x.is_integer():
        x=int(x)
    if y.is_integer():
        y=int(y)
    if z.is_integer():
        z=int(z)
    if x == (y+z) or y == (x+z) or z == (y+x):
        return True
    return False

