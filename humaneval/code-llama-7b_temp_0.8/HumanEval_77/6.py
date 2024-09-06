
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
    import math

    def is_perfect_cube(x):
        '''
        Returns True if x is a perfect cube, otherwise False.
        Note: you may assume the input is always valid.
        '''
        ans = int(round(x**(1./3)))
        return ans**3 == x

    if a < 0:
        a = -a

    if is_perfect_cube(a):
        return True

    return False
