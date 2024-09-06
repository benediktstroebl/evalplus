
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
    return False

    a = int(input())
    if a < 0:
        a = a * (-1)
    temp = a
    for i in range(1, 1000000):
        if a == i * i * i:
            return True
        a = a + 1
    return False
    return













































































































































































