
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
    # Check if the number is negative
    if a < 0:
        return True
    
    # Check if the number is a power of 3
    if a % 3 == 0:
        return True
    
    # Check if the number is a power of 2
    if a % 2 == 0:
        return True
    
    # Check if the number is a power of 2 and a power of 3
    if a % 2 == 0 and a % 3 == 0:
        return True
    
    # Check if the number is a power of 3 and a power of 4
    if a % 3 == 0 and a % 4 == 0:
        return True
    
    # Check if the number is a power of 4 and a power of 5
    if a % 4 == 0 and a % 5 == 0:
        return True
    
    # Check if the number is a power of 5 and a power of 6
    if a % 5 == 0 and a % 6 == 0:
        return True
    
    # Check if the number is a power of 6 and a power of 7
    if a % 6 == 0 and a % 7 == 0:
        return True
    
    # Check if the number is a power of 7 and a power of 8
    if a % 7 == 0 and a % 8 == 0:
        return True
    
    # Check if the number is a power of 8 and a power of 9
    if a % 8 == 0 and a % 9 == 0:
        return True
    
    # Check if the number is a power of 9 and a power of 10
    if a % 9 == 0 and a % 10 == 0:
        return True
    
    # Check if the number is a power of 10 and a power of 11
    if a % 10 == 0 and a % 11 == 0:
        return True
    
    # Check if the number is a power of 11 and a power of 12
    if a % 1
