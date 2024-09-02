
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
        a_1 = a ** (1/3)
        a_1 = int(a_1)
        if a_1 ** 3 == a:
            return True
        else:
            return False
    elif a < 0:
        a_1 = (-1) * a
        a_1 = a_1 ** (1/3)
        a_1 = int(a_1)
        if a_1 ** 3 == (-1) * a:
            return True
        else:
            return False
    else:
        return True

