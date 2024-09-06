
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
    # Check if all numbers are integers
    if all(isinstance(n, int) for n in [x, y, z]):
        # Check if one number is equal to the sum of the other two
        if x == (y + z) % 2:
            return True
        elif y == (x + z) % 2:
            return True
        elif z == (x + y) % 2:
            return True
    return False
