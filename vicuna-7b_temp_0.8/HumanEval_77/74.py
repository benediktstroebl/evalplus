
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
    # the first 64 numbers are relatively prime to 64
    # if a is divisible by any of them, it's not a cube
    for num in range(1, 65):
        if num % a == 0:
            return False
    return True
