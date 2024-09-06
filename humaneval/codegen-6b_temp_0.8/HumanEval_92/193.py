
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
    return x == y + z or x == (y + z) / 2 or x == (y + z) / 4 or x == (y + z) / 8 or x == (y + z) / 16 or x == y or x == z or x == y / 4 or x == z / 4 or x == y / 8 or x == (y / 8) or x == z / 8 or x == (z / 8) or y / 4 == z / 4 or y / 8 == z / 8
   
    
    


    
    
    
    
    
    
