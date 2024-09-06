
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
    n = 0
    while a > 0:
        n = n + 1
        a = a / 10
    if (a == 1):
        return True
    elif n % 2!= 0:
        return False
    else:
        return (int(a**((n/2)+1))) == a
        






