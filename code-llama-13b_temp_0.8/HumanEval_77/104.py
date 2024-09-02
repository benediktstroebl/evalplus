
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
    from math import pow, ceil
    from math import floor
    from math import sqrt
    x=pow(ceil(sqrt(a)),2)
    y=pow(floor(sqrt(a)),2)
    if x==a or y==a:
        return True
    else:
        return False

