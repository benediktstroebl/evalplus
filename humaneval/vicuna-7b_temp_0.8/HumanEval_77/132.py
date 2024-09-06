
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
    # Counter for storing number of cubes found
    counter = 0
    
    # Loop through all integers between 1 and 100 and check if a is the cube of any of them
    for x in range(1, 101):
        if a**3 == x:
            counter += 1
    
    return counter > 1
