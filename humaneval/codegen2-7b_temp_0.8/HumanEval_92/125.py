
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
    return (x + y == z) or (x + y == z+1) or (x + y == z-1) or (x == z) or (x == z+1) or (x == z-1) or (x == y) or (x == y+1) or (x == y-1) or (y == z) or (y == z+1) or (y == z-1) or (y == x) or (y == x+1) or (y == x-1)
