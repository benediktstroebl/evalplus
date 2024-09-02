
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
    if x == y + z or x == y - z or x == z - y or z == y - x or x == z + y or z == x + y or y == z + x:
        return True
    if x % 1 != 0 or y % 1 != 0 or z % 1 != 0:
        return False
    return -1 < x - y < 1 or -1 < x - z < 1 or -1 < z - y < 1 or 1 > x - y > -1 or 1 > x - z > -1 or 1 > z - y > -1 or -1 < x + y < 1 or -1 < x + z < 1 or -1 < z + y < 1 or 1 > x + y > -1 or 1 > x + z > -1 or 1 > z + y > -1:
    return False
    
import unittest
