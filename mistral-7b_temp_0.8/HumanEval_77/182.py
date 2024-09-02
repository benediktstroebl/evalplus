
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
    '''
    (a, n) in (0, 0), (1, 1), (2, 1), (4, 1), (8, 2), (27, 3), (16, 2), (100, 3)

    n = 1 + 2 * (a**(1/3) - 1)
    '''
    n = int(a**(1/3) + 1)
    if a == n**3:
        return True
    else:
        return False
