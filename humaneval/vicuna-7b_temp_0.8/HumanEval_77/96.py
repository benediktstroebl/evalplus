
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
    # Your code here
    
    # check if a is negative
    if a < 0:
        return True
    
    # check if a is even
    if a % 2 == 0:
        return False
    
    # check if a is a power of 3
    for i in range(3, int(a ** 0.5) + 1):
        if a % i == 0:
            return True
    
    # check if a is a power of 2
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return True
    
    # check if a is a power of 5
    for i in range(5, int(a ** 0.5) + 1):
        if a % i == 0:
            return True
    
    # check if a is a power of 7
    for i in range(7, int(a ** 0.5) + 1):
        if a % i == 0:
            return True
    
    # check if a is a power of 11
    for i in range(11, int(a ** 0.5) + 1):
        if a % i == 0:
            return True
    
    # check if a is a power of 13
    for i in range(13, int(a ** 0.5) + 1):
        if a % i == 0:
            return True
    
    # check if a is a power of 17
    for i in range(17, int(a ** 0.5) + 1):
        if a % i == 0:
            return True
    
    # check if a is a power of 19
    for i in range(19, int(a ** 0.5) + 1):
        if a % i == 0:
            return True
    
    # check if a is a power of 25
    for i in range(25, int(a ** 0.5) + 1):
        if a % i == 0:
            return True
