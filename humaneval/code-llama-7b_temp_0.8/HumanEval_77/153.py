
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
    # solution 1
    # return a in set(map(lambda x: x ** 3, range(a // 3 + 1)))

    # solution 2
    return a ** (1 / 3) == int(a ** (1 / 3))

