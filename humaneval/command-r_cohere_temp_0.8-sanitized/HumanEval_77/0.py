def iscube(a):
    '''
    Checks if integer a is a cube of some integer number.
    '''
    # Cube roots are always positive, so we can ignore the sign
    a = abs(a) 
    root = a ** (1/3)
    return root.is_integer()