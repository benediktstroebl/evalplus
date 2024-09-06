
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
    # Note: how to calculate a**3?
    # from math import sqrt
    # return a**3 == int(sqrt(a))**3
    # this is just shortcut

    return a**3 == int(a**(1/3))**3

