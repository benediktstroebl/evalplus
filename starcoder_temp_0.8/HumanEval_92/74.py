
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
    result=[]
    for i in [x,y,z]:
        if i==x+y or i==x+z or i==y+z:
            if type(i)==int:
                result.append(True)
            else:
                result.append(False)
        else:
            result.append(False)
    if True in result:
        return True
    return False


