
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
    # Check if a is 0
    if a == 0:
        return True
    # Check if a is a positive cube
    if a > 0 and (a**3 % 1) == 0:
        return True
    # Check if a is a negative cube
    if a < 0 and (a**3 % 1) == 0:
        return True
    # If a is not a cube, it is not a cube
    return False
