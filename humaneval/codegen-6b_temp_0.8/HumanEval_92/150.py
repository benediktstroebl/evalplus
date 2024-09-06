
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
    a1 = True
    a2 = True
    a3 = True
    a4 = True
    a5 = True
    a6 = True
    a7 = True
    a8 = True
    if isinstance(x, int):
        a1 = True
    else:
        a1 = False

    if isinstance(y, int):
        a2 = True
    else:
        a2 = False

    if isinstance(z, int):
        a3 = True
    else:
        a3 = False

    if x < 0:
        a4 = False
    elif y < 0:
        a5 = False
    elif z < 0:
        a6 = False

    return a1 and a2 and a3 and a4 and a5 and a6
