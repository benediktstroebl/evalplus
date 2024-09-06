
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
    # code to check if a is a cube of an integer
    # if a is a cube of some integer, return True
    # if a is not a cube of any integer, return False
    # if a is not a positive integer, return True
    # if a is not a non-negative integer, return True
    # if a is not a number, return False
    
    # code to check if a is a cube of some integer
    if a**3 % a == 0:
        return True
    
    # code to check if a is not a cube of any integer
    if a**3 != a * a**2:
        return True
    
    # code to check if a is not a positive integer
    if a < 0:
        return True
    
    # code to check if a is not a non-negative integer
    if a < 0:
        return True
    
    # code to check if a is not a number
    if a not in (int(a), float(a)):
        return False
    
    return True