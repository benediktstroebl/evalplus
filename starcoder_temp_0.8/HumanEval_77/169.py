
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
    a = abs(a)
    if a == 0:
        return True
    elif a % 4!= 0:
        return False
    elif a < 0:
        return iscube(-a)
    else:
        n = 0
        while a > 0:
            n += 1
            a /= 4
        return n % 2 == 0
