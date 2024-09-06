
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
    sum1=x+y
    sum2=x+z
    sum3=y+z
    if(x==sum1 or x==sum2 or x==sum3) and y==sum1 or y==sum2 or y==sum3) and z==sum1 or z==sum2 or z==sum3):
        return True
    else:
        return False
