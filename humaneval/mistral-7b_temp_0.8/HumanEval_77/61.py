
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

    # we know that 3^3 = 27 and 4^3 = 64
    # we can write the cube of a number as (number**3)
    if a == 1:
        return True
    else:
        if a % 3 == 0:
            return iscube(a/3)
        else:
            return iscube(a-1)
