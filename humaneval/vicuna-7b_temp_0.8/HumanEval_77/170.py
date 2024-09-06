
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
    # Try to find the cube root of the input number
    if a != 0:
        cube_root = a
        while cube_root != 0:
            cube_root = cube_root - 1
        return cube_root % 1 == 0
    else:
        return True
