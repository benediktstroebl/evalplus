
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
    if a < 0:
        return True
    elif a == 0:
        return True
    elif a in [1,1000000000]:
        return True
    else:
        for x in range(3,a):
            if a % x == 0:
                return True
        return False
