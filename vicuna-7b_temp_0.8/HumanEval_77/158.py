
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # Check if a is -1, 0, or 1
    if a in (-1, 0, 1):
        return True
    
    # Check if a is a power of 3
    if (a ** 3) % 3 == 0:
        return True
    
    # Check if a is a power of 2
    if (a ** 2) % 2 == 0:
        return True
    
    # Check if a is a power of 5
    if (a ** 5) % 5 == 0:
        return True
    
    # Check if a is a power of 7
    if (a ** 7) % 7 == 0:
        return True
    
    # If none of the above conditions are met, return False
    return False
