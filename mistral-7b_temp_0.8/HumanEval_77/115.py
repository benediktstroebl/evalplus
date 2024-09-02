
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
    if a == 1:
        return True
    if a % 10 == 1 or a % 10 == 6 or a % 10 == 8:
        return False
    if a % 10 == 7:
        a = a - 7
        if a % 10 == 2:
            return False
        return True
    if a % 10 == 2:
        a = a - 2
        if a % 10 == 1:
            return False
        return True
    if a % 10 == 5:
        a = a - 5
        if a % 10 == 4 or a % 10 == 6 or a % 10 == 7:
            return False
        return True
    if a % 10 == 4:
        a = a - 4
        if a % 10 == 3:
            return False
        return True
    if a % 10 == 3:
        a = a - 3
