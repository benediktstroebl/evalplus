
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
    #y,z=sum(y,z),sum(y,z)
    #y,z=int(y),int(z)
    #y,z=int(y),int(z)
    #return y==z or z==sum(y,z) or y==sum(y,z)

    #return y==z or z==sum(y,z) or y==sum(y,z)
    #return  (z==sum(y,z) or y==z) and type(y)==type(z)==type(z+y)==int
    return  (z==sum(y,z) or y==z) and type(y)==type(z)==type(z+y)
    #return all([type(y)==type(z)==type(z+y)==int,y==z,y==z+z,z==y+y])
    return (type(y)==type(z)==type(z+y)==int and y==z or y==z+z or z==y+y)
