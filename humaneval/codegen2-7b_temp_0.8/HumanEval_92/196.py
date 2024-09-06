
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
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    e = x // y
    f = x ** y
    
    if a == (x + y) and b == (x - y) and c == (x * y) and d == (x / y) and e == (x // y) and f == (x ** y):
        return True
    else:
        return False
        
    
    
