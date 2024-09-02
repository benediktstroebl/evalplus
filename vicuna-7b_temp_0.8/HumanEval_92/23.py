
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
    # Check the first number
    if x == sum(y+z) or abs(x-sum(y+z)) <= 0.0001:
        return True
    # Check the second number
    if y == sum(x+z) or abs(y-sum(x+z)) <= 0.0001:
        return True
    # Check the third number
    if z == sum(x+y) or abs(z-sum(x+y)) <= 0.0001:
        return True
    return False
