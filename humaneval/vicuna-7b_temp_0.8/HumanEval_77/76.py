
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
    # First, let's check if a is equal to -1, 0, or 1.
    # If it is, we know it is a cube.
    if a == -1 or a == 0 or a == 1:
        return True

    # Next, we'll check if a is a power of any integer between 2 and 31.
    # If it is, we know it is a cube.
    for i in range(2, 32):
        if a % i == 0:
            return True

    # If we've checked all of the above and a is still unknown, 
    # we'll just have to assume it's not a cube.
    return False
