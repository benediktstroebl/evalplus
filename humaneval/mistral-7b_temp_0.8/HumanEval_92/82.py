
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
    # 1st attempt
    # if x == (y + z) or y == (x + z) or z == (x + y):
    #     return True
    # return False
    #
    # 2nd attempt
    # if x == (y + z) or y == (x + z) or z == (x + y):
    #     return True
    # return False

    # 3rd attempt
    # if x == (y + z) or y == (x + z) or z == (x + y):
    #     return True
    # return False

    # 4th attempt
    # if type(x) == int and type(y) == int and type(z) == int and (x == (y + z) or y == (x + z) or z == (x + y)):
    #     return True
    # return False
    # 5th attempt
    # return any(x == y + z for x, y, z in zip((x, y, z), (y, z, x), (z, x, y)))
    return
