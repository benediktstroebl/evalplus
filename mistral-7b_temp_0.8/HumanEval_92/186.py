
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
    # 1
    def any_int(x, y, z):
        if (x == y + z and y == x + z and z == x + y):
            return True
        elif (x == y + z and x == x + y and y == z + x):
            return True
        elif (x == y + z and x == x + z and z == y + x):
            return True
        elif (x == y + z and x == y + z and y == x + z):
            return True
        elif (x == y + z and x == y + z and z == x + y):
            return True
        elif (x == y + z and y == x + z and z == x + y):
            return True
        elif (x == y + z and y == x + z and z == y + x):
            return True
        else:
            return False


    # 2
    def any_int(x, y, z):
        if (x == y + z and y == x + z and z == x + y):
            return True
        elif
