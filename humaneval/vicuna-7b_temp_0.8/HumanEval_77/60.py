
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
    # this is a simple way to check if a^3 is an integer
    if a % 3 == 0:
        return True
    # if a^3 is not an integer, we can check if a is a power of 3
    if a % 3 != 0:
        for i in range(2, int(math.sqrt(a))+1):
            if a % i == 0:
                return True
    return False
