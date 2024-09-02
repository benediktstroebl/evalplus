
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
    if a in range(-10, 1001):
        if a**3 == 0:
            return False
        elif a**3 < 0:
            return True
        else:
            return a == 1 or iscube(a**(1/3))
    else:
        return False
