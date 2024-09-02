
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
    if a == 0 or a == 1 or a == -1:
        return True
    elif a < 0:
        return iscube(-a)
    else:
        for i in range(1, a):
            if a**(1/3) == int(a**(1/3)):
                return True
            else:
                return False
