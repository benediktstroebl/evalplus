
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
    # Check if the first two numbers are equal
    if x == y:
        return True

    # Check if the sum of the first two numbers is equal to the third number
    if x + y == z:
        return True

    # Check if the third number is an integer
    if not isinstance(z, int):
        return False

    # If the above three conditions are met, return True
    return True