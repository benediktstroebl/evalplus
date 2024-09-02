
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
    #first make sure all arguments are integers
    if (x.is_integer() and y.is_integer() and z.is_integer()):
        #then find the sum of the arguments
        sum=x+y+z
        #now compare the sum to the arguments
        if (x==sum or y==sum or z==sum):
            return True
        else:
            return False
    else:
        return False
    
