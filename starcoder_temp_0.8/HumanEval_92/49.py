
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
    return (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)) or (isinstance(x, float) and isinstance(y, float) and isinstance(z, float)) or (isinstance(x, complex) and isinstance(y, complex) and isinstance(z, complex)) or (isinstance(x, float) and isinstance(y, float) and isinstance(z, int)) or (isinstance(x, int) and isinstance(y, int) and isinstance(z, float)) or (isinstance(x, int) and isinstance(y, float) and isinstance(z, float)) or (isinstance(x, int) and isinstance(y, float) and isinstance(z, int)) or (isinstance(x, float) and isinstance(y, int) and isinstance(z, int)) or (isinstance(x, float) and isinstance(y, int) and isinstance(z, float)) or (isinstance(x, float) and isinstance(y, float) and isinstance(z, int)) or (isinstance(x, int) and isinstance(y, complex) and isinstance(z, complex)) or (isinstance(x, float) and isinstance(y, complex) and isinstance(z, complex)) or (isinstance(x, complex) and isinstance(y, int) and isinstance(z, complex)) or (isinstance(x, complex) and isinstance(y, float) and isinstance(z, complex)) or (isinstance(x, complex) and isinstance(y, complex) and isinstance(z, int)) or (isinstance(x, complex) and isinstance(y, complex) and isinstance(z, float)) or (isinstance(x, complex) and isinstance(y, complex) and isinstance(z, complex))
