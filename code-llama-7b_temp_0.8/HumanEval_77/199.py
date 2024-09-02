
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
    # R1
    #a = abs(a)
    #if a ** (1/3) % 1 == 0:
    #    return True
    #else:
    #    return False
    # R2
    #return abs(a ** (1/3)) % 1 == 0
    # R3
    #return abs(a ** (1/3)) * 10 % 1 == 0
    # R4
    #return abs(a) % (a ** (1/3)) == 0
    # R5
    #return a % (a ** (1/3)) == 0

