
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
    # 1 
    # return a >= 0 and a == round(a**(1/3))**3
    # 2
    # return a >= 0 and int(a**(1/3))**3 == a
    # 3
    # return a >= 0 and str(a)[:-1] == str(a**(1/3))[:-1] and str(a)[-1] == str(a**(1/3))[-1]
    # 4
    # return a >= 0 and a in [i**3 for i in range(a+1)]

