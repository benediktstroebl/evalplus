
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
    #---------------------------------------------------
    # The following is a wrong answer and is commented out.
    # This is because 27 in base 10 is not the same as
    # 11111 in base 2.
    # return bin(a)[2:].count('1')==3
    #---------------------------------------------------

    # This is the correct answer.
    # int(a**(1/3))==a/a**(1/3)
    # a/a**(1/3) is integer if and only if a is a cube.
    return int(a**(1/3))*a**(1/3)==a
