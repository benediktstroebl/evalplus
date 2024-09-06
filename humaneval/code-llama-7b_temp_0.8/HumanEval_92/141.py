
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
    
    if (int(x) + int(y) == z or int(x) + int(z) == y or int(z) + int(y) == x) and (int(x) + int(y) == x or int(x) + int(y) == y or int(x) + int(y) == z) and (int(x) + int(y) == x or int(x) + int(y) == y or int(x) + int(y) == z):
        return True
    else:
        return False

