
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
    if a % 100 > 0:
        return True
    if a % 100 < 0:
        return True
    if a % 100 == 0:
        return a % 100 == 0 or (a % 100 // 2 == 0 and (a % 100 // 3 == 0 or a % 100 // 4 == 0))
    return False
