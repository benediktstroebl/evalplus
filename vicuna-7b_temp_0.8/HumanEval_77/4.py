
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
    # your code here
    
    # check if a is a perfect square
    if a**2 % a == 0:
        return True
    
    # check if a is a power of 3
    if a == 3**k for k in range(0, log(a, 3)) + 1:
        return True
    
    # check if a is a power of 2
    if a == 2**k for k in range(0, log(a, 2)) + 1:
        return True
    
    # check if a is a power of 4
    if a == 4**k for k in range(0, log(a, 4)) + 1:
        return True
    
    # check if a is a power of 5
    if a == 5**k for k in range(0, log(a, 5)) + 1:
        return True
    
    return False
