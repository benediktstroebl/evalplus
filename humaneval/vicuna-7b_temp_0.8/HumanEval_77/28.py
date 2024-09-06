
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
    # Check if a is a perfect square
    if (a**2) % 2 == 0:
        return True

    # Check if a is a prime number
    if (a % 2) == 1:
        return True

    # Check if a is a cube of a prime number
    if iscube(a % 2) and a % 2 != 0:
        return True

    return False
