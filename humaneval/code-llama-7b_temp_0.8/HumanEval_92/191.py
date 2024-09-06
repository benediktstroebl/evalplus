
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
    
    return (x+y==z and str(x).isdigit() and str(y).isdigit() and str(z).isdigit()) or (x+z==y and str(x).isdigit() and str(z).isdigit() and str(y).isdigit()) or (y+z==x and str(y).isdigit() and str(z).isdigit() and str(x).isdigit()) 
