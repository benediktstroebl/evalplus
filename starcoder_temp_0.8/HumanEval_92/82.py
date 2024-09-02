
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
    # Your code here
    a = [x,y,z]
    b = [x+y,x+z,y+z]
    if any(i.is_integer() for i in a) and any(i.is_integer() for i in b):
        return any(i == j for i in a for j in b)
    else:
        return False

