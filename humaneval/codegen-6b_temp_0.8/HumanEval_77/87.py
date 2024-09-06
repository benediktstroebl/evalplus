
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
    # save the first digit and multiply the result to it
    value = int(str(a)[0])
    # if the first digit is 1 or -1, we return True
    if value == 1 or value == -1:
        return True
    # change the first digit to -1 and add the result to the result
    # if the result is -1, we return True
    elif value == 0:
        return True
    else:
        return False
