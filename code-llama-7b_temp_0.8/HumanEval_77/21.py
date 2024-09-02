
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
    # first check if the input is zero
    # if so return True
    if a == 0:
        return True
    # use the built in functions abs() and pow()
    # this checks if the abs of the input powered to 1/3
    # is equal to the input
    return abs(pow(a,1/3)) == a
    
    return False
