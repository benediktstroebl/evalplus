
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
    # If the input is 0 or a negative number, return True
    if a < 0:
        return True
    # Otherwise, check if the input is a cube of some integer number
    for num in range(1, a+1):
        if pow(a, num, 100) == num*num:
            return True
    return False