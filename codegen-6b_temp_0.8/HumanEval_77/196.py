
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
    # return a ** 3 == a * a * a;
    return a ** 3 == (a * a * a)
    # return True if (a == 1) or (a == -1) else False
    # return True if (a in [1, -1]) else False
    # iterate through all numbers and check if this is a valid cube
    # return sum(int(i) ** 3 == int(i * i * i) for i in range(-10, 10))
