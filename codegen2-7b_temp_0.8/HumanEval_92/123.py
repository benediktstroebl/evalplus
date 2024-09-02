
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
    
    
    if (x+y==z or x+y==0 or y+z==0) or (x==y and x==z) or (x==y and y==z) or (x==y and y!=z) or (x==y and z!=y) or (y==z and x!=y) or (y==z and y!=x) or (y==z and z!=x) or (z==x and x!=y) or (z==x and y!=z):
        return True
    else:
        return
