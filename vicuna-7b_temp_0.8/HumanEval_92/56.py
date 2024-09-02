
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
    if x + y == z:
        if abs(x-y) == 1 and abs(x-z) == 1:
            return True
        elif abs(x-y) == 2 and abs(x-z) == 2:
            return True
        elif abs(x-y) == 3 and abs(x-z) == 3:
            return True
        else:
            return False
    else:
        return False
