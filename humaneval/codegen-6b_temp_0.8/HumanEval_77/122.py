
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
    a %= 360
    if a == 0:
        return True
    is_divided = [False] * 360
    for i in range(1, 360):
        if (a % i) == 0:
            if is_divided[i] == False:
                is_divided[i] = True
            if (a // i) == i:
                is_divided[i] = True
                is_divided[i // 360] = True
    return is_divided[a % 360]
