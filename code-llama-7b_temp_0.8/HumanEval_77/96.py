
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
    i, j, k = 0, 0, 0
    while i <= a:
        j = int(a ** (1 / 3))
        if i * i * i == a:
            return True
        else:
            i += 1

    return False
