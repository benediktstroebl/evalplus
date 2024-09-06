
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
    return int(x+y) == int(y+z) or int(x+z) == int(y+x) or int(x+y) == int(z+x) or int(x+z) == int(y+x) or int(y+z) == int(x+y) or int(y+z) == int(x+y) or int(x+y) == int(y+z) or int(x+z) == int(y+x) or int(y+z) == int(x+y) or int(y+z) == int(x+y) or int(x+y) == int(y+z) or int(x+z) == int(y+x) or int(y+z) == int(x+y) or int(y+z) == int(x+y) or int(x+y) == int(y+z) or int(x+z) == int(y+x) or int(y+z) == int(x+y) or int(y+z) == int(x+y) or int(x+y) == int(y+z) or int(x+z) == int(y+x) or int(y+z) == int(x+y) or int(y+z) == int(x+y) or int(x+y) == int(y+z) or int(x+z) == int(y+x) or int(y+z) == int(x+y) or int(y+z) == int(x+y) or int(x+y) == int(y+z) or int(x+z) == int(y+x) or int(y+z) == int(x+y) or int(y+z) == int(x+y) or int(x+y) == int(y+z) or int(x+z) == int(y+x) or int(y+z) == int(x+y) or int(y+z) == int(x+y) or int(x+y) == int(y+z) or int(x+z) == int(y+x) or int(y+z)
