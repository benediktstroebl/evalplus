
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
    if a == 0:
        return True
    elif a < 0:
        for i in range(1, abs(a)):
            if i**3 == abs(a):
                return True
        return False
    else:
        for i in range(1, a):
            if i**3 == a:
                return True
        return False
