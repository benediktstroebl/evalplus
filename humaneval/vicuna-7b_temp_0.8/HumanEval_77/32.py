
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
    # if a is a cube of some integer, then its always positive and divisible by 3
    if a > 0 and a % 3 == 0:
        return True
    # if a is not a cube of any integer, then it must be odd,
    # and a % 3 will always return 1
    if a % 3 == 1:
        return True
    # if a is not a cube of any integer,
    # and a % 3 will always return 0
    if a % 3 == 0:
        return True
    return False