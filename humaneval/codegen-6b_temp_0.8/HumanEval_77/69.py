
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
    # if a == 0:
    #     return True
    # next_int = isquare(a)
    # if next_int == a:
    #     return True
    # else:
    #     return False
    # if a < 0:
    #     return False
    # for i in range(1, a/2+1):
    #     next_int = get_int(a, i)
    #     if next_int == a:
    #         return True
    #     if next_int != a:
    #         return False
    # return True
    return _iscube(a)
