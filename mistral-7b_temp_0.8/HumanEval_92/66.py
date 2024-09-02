
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
    # your code here
    if x+y == z and x.is_integer() and y.is_integer() and z.is_integer():
        return True
    else:
        return False
    # Check if the sum of the first two arguments is equal to the third argument.
    # Check if the first argument is an integer.
    # Check if the second argument is an integer.
    # Check if the third argument is an integer.
    # Return True if all three conditions are met.
    # Return False otherwise.

