
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
    cube = (a**(1/3))*1000
    # The following codes are to find the 2-digits of the floating number
    if cube.is_integer():
        return True
    else:
        cube = int(str(cube).split('.')[0])
        return True
