
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
    return int(x) + int(y) == z

    # YOUR CODE HERE
    # return (int(x) + int(y)) == int(z) and int(x) != 0 and int(y) != 0 and int(z) != 0
    # return (int(x) + int(y)) == int(z) and int(x) != 0 and int(y) != 0 and int(z) != 0
