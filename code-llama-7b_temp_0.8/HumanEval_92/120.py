
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
    
    if int(x)==int(y)+int(z) or int(y)==int(x)+int(z) or int(z)==int(x)+int(y):
        return True
    elif int(x)==int(y)+int(z) or int(y)==int(x)+int(z) or int(z)==int(x)+int(y):
        return True
    elif x==y or y==z or x==z:
        return False
    else:
        return True
    


