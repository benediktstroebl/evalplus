
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
    if (x == int(y + z)) or (y == int(x + z)) or (z == int(x + y)):
        return True
    else:
        return False
  
  
  
any_int(3, 2, 2) ➞ False

any_int(10, 2, 2) ➞ True

any_int(10, 2, 4) ➞ False

any_int(10, 1, 1) ➞ True

any_int(10, 2.3, 2) ➞ True

any_int(10, 2, 2.2) ➞ False

any_int(1, 2, 3) ➞ False

any_int(2.2, 2, 2) ➞ False