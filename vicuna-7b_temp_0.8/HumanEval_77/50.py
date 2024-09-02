
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
    if a > 0:
        if a**3 % 1 == 0:
            return True
        for i in range(2, int(a**0.5) + 1):
            if a**i % 1 == 0:
                return True
    return False
