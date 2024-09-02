
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
    if (type(x) == int) or (type(y) == int) or (type(z) == int):
        if x == y + z or x == y - z or x == z - y:
            return True
        return False
    
    if type(x) == int or type(x) == float:
        if x == y + z or x == y - z or x == z - y:
            return True
        return False
    
    if type(y) == int or type(y) == float:
        if y == x + z or y == x - z or y == z - x:
            return True
        return False
    
    if type(z) == int or type(z) == float:
        if z == x + y or z == x - y or z == y - x:
            return True
        return False
    
    
    
    
    
    
    
    
    
    
    
