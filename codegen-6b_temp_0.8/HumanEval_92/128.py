
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
    return any([
        1 == sum([x, y]) and type(x) is int and type(y) is int,
        1 == sum([x, z]) and type(x) is int and type(z) is int,
        1 == sum([y, z]) and type(y) is int and type(z) is int
    ])
