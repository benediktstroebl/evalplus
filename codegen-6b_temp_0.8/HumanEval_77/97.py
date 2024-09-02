
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
    #if a == 1:
    #    return True
    #elif a == 2:
    #    return False
    #elif a < 0:
    #    return (abs(a) ** 3) % m == 0
    #else:
    #    return (a ** 3) % m == 1
    return a ** 3 % m == 1
