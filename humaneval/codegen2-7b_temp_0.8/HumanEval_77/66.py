
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
    n = abs(a)
    
    if n == 1:
        return True
    elif n == 0 or n == 1 or n == 4 or n == 9 or n == 16 or n == 25 or n == 36 or n == 49 or n == 64:
        return True
    elif n == 3 or n == 6 or n == 10 or n == 15 or n == 21 or n == 28 or n == 36 or n == 45 or n == 55 or n == 66 or n == 78 or n == 91 or n == 105:
        return True
    else:
