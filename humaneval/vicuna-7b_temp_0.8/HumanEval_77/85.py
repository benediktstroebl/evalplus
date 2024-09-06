
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
    # The output is True if a is the cube of an integer
    # that is not divisible by 3.
    # The condition 3**2 % a == 0 is equivalent to 3**2 > a.
    return 3**2 > a