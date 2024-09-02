
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
    # First, we check if the input is a negative number
    if a < 0:
        return True
    
    # Next, we check if the input is 0
    if a == 0:
        return True
    
    # Now we check if the input is a power of 3
    if a % 3 == 0:
        return True
    
    # Finally, we check if the input is a power of 2
    if a % 2 == 0:
        return True
    
    return False