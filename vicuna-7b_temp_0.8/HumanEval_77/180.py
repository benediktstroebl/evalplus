
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
    if a > 1:
        x = a
        while x > 1:
            x = x - 1
            if x % 2 != 0:
                return False
        return True
    elif a == 1:
        return True
    else:
        return False
