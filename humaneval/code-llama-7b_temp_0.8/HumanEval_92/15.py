
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
    if (x== y+z) or (y== x+z) or (z== x+y) or (x== y== z) or (x== z== y) or (y== z== x) or (x== y== z==0) or (x== y== z==1) or (x== y== z==2) or (x== y== z==3) or (x== y== z==4) or (x== y== z==5) or (x== y== z==6) or (x== y== z==7) or (x== y== z==8) or (x== y== z==9) or (x== y== z==10):
        return True
    elif (x+y+z == 0) or (x+y+z == 1) or (x+y+z == 2) or (x+y+z == 3) or (x+y+z == 4) or (x+y+z == 5) or (x+y+z == 6) or (x+y+z == 7) or (x+y+z == 8) or (x+y+z == 9) or (x+y+z == 10) or (x+y+z == 11) or (x+y+z == 12) or (x+y+z == 13) or (x+y+z == 14) or (x+y+z == 15) or (x+y+z == 16) or (x+y+z == 17) or (x+y+z == 18) or (x+y+z == 19) or (x+y+z == 20):
        return False
    else:
        return False
