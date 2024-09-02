
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
    # check if a is a power of 3
    if a % 3 == 0:
        return True
    # check if a is a power of 2
    if a % 2 == 0:
        return True
    # check if a is a power of 5
    if a % 5 == 0:
        return True
    # check if a is a power of 7
    if a % 7 == 0:
        return True
    # check if a is a power of 9
    if a % 9 == 0:
        return True
    # check if a is a power of 11
    if a % 11 == 0:
        return True
    return False
