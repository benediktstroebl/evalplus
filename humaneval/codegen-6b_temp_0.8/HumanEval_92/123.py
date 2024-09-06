
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
    return (int(x) + int(y) == int(z)) or (int(y) + int(z) == int(x)) or (int(x) + int(z) == int(y))

    # if (y + z == int(x)) or (z + x == int(y)) or (x + y == int(z)):
    #     return True
    # else:
    #     return False
    # return any([y + z == int(x), z + x == int(y), x + y == int(z)])

import itertools
