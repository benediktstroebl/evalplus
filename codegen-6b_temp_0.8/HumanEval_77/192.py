
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
    return a ** 3 == a
    # or a ** 3 == eval(str(a)+'**3')
    # or a % 3 == 0
    # or a % 4 == 0
    # return a % 2 == 0
    # return a % 4 == 0
    # or a % 2 == 0
    # or a % 4 == 0
    # or a % 2 == 0
    # or a % 4 == 0
    # or a % 2 == 0
