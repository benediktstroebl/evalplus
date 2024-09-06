
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

    #First I will check to make sure they are integers
    if type(x) == int and type(y) == int and type(z) == int:
        #If the second number is equal to the sum of the other two numbers return true
        if z == x + y:
            return True
        #If the third number is equal to the sum of the other two numbers return true
        if z == y + x:
            return True
        #If the first number is equal to the sum of the other two numbers return true
        if z == y + x:
            return True
        #Any other case return false
        return False
    #Any other case return false
    return False
    
