
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
    # This implementation is not efficient, as it uses a lot of nested if-statements.
    # A more efficient approach would be to use a recursive function or a more sophisticated algorithm.
    if x == y + z or x == y - z or x == z + y or x == z - y:
        return True
    return False