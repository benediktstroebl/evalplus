
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
    # Using a nested loop for efficiency
    for i in range(1, a):
        for j in range(1, a-i+1):
            for k in range(1, i-1, -1):
                if a % (i*j*k) == 0:
                    return True
    return False