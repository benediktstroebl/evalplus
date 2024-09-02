
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
    
    if a == 1:
        return True
    elif a % 1 == 0 and a % 2 == 0:
        return False
    elif a % 1 == 0 and a % 3 == 0:
        return False
    elif a % 1 == 0 and a % 4 == 0:
        return False
    elif a % 3 == 0 and a % 4 == 0:
        return False
    else:
        return
