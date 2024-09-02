
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
    return (x + y == z or y + z == x or x + z == y) and all([x, y, z].is_integer())

    # return any([x + y == z or y + z == x or x + z == y for x, y, z in zip([x, y, z], [x, y, z])])


    # a = [x, y, z]
    # if a.count(a.sum()):
    #     if all([x.is_integer() for x in a]):
    #         return True
    #     else:
    #         return False
    # else:
    #     return False



































































































