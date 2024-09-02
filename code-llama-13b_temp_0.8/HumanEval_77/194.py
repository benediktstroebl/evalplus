
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
        i = 0
        while i**3 < a:
            i += 1
        return i**3 == a
    elif a < 0:
        i = -1
        while i**3 > a:
            i -= 1
        return i**3 == a
    elif a == 0:
        return True
