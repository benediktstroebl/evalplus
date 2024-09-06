
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
    # Return True if n is a perfect cube.
    # y is the integer part of the cube root of n
    y = int(n ** (1 / 3))
    # return n is a perfect cube and y**3 == n
    return n == y**3


