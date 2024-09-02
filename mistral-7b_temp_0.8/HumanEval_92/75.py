
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
    return True if int(x) == y + z or int(y) == x + z or int(z) == x + y else False


    #Solution 1

    return (int(x) == (y + z) or int(y) == (x + z) or int(z) == (x + y)) and int(x) and int(y) and int(z)

    #Solution 2

    return (x == y + z or y == x + z or z == x + y) and (x.isdigit() and y.isdigit() and z.isdigit())

    #Solution 3

    x, y, z = int(x), int(y), int(z)
    return x == y + z or y == x + z or z == x + y and x and y and z

    #Solution 4

    return (int(x) == y + z or int(y) == x + z or int(z) == x + y) and int(x) and int(y) and int(z)
