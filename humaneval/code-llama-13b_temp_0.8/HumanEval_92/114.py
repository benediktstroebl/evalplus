
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
    if sum([x,y,z]) in [x,y,z]:
        if sum([x,y,z]) == x or sum([x,y,z]) == y or sum([x,y,z]) == z:
            if x==int(x) and y==int(y) and z==int(z):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

