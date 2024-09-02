
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

    x = int(x)
    y = int(y)
    z = int(z)

    return (x+y == z) or (y+z == x) or (x+z == y)
    #other way of solving:
    #return (x + y) == z or (x + z) == y or (y + z) == x


    '''
    #Create a function that takes a number and returns true if it's not divisible by 5 or 13, and false in any other case.
    
    Examples
    not_divisible(34) ➞ True
    
    not_divisible(25) ➞ False
    
    not_divisible(45) ➞ False
    
    not_divisible(84) ➞ True
    
    not_divisible(11) ➞ False
    
    '''
    #def not_divisible(x):
    #    return x % 5 != 0 and x % 13 != 0
    #    return
