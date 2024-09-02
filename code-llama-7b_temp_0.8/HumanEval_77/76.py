
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
    def cube(a):
        if a == 0:
            return a
        if a > 0:
            a = a / 6.0
            return int(a) ** 3
        if a < 0:
            a = a / 6.0
            return -1 * int(a) ** 3
    return cube(a) == a
