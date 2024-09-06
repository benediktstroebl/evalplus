
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
    from math import floor, ceil
    #print('input:',a)
    if a < 0:
        a = a * -1
        #print('a:',a)
        if int(floor(a ** (1/3))) * int(floor(a ** (1/3))) * int(floor(a ** (1/3))) == a:
            return True
    if a > 0:
        if int(floor(a ** (1/3))) * int(floor(a ** (1/3))) * int(floor(a ** (1/3))) == a:
            return True
    return False

