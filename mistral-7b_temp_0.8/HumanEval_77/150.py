
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
        a = abs(a)
    if a == 1:
        return True
    if a == 2 or a == 3:
        return False
    elif a % 2 == 0:
        return False
    else:
        return a == int(a ** (1 / 3)) ** 3

