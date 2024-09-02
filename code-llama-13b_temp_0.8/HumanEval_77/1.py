
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
    from math import log10, floor
    
    x = log10(abs(a)) // 1
    x = 10**(x-1)
    x = int(a / x)
    if a < 0:
        x = -1 * x
    return x**3 == a
