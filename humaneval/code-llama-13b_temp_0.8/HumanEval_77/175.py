
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
    def intCubeRoot(n):
        # apporximate the cube root of n using Newton's method
        r = n ** (1./3)
        while abs(r**3 - n) > 1e-8:
            r = r - (r**3 - n)/(3*r**2)
        return int(r)
    
    x = intCubeRoot(a)
    return a == x**3
