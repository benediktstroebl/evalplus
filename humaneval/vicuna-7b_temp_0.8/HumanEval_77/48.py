
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
    # implement your solution here
    
    # check if a is 1, 2, 0, or a power of 2
    if a in (1, 2, 0, set([2])) or a % 2 != 0:
        return False
    # check if a is a power of 3
    if a != 3 and a != 9 and a != 27:
        return False
    # check if a is the cube of a number between 1 and 100
    for i in range(1, 100):
        if a == i**3:
            return True
    # check if a is the cube of a number between -100 and 100
    for i in range(-100, 101):
        if a == i**3:
            return True
    # check if a is the cube of a number between -100 and 100 and with special values
    for i in range(-100, 101):
        if a == i**3 and i in (0, 1, -1):
            return True
    # check if a is the cube of a number between -100 and 100
    for i in range(-100, 101):
        if a == i**3 and (i**2 == a or a == -i**2):
            return True
    # check if a is the cube of a number between -100 and 100
    for i in range(-100, 101):
        if a == i**3 and (i**2 == -a or a == -i**2):
            return True
    # check if a is the cube of a number between -100 and 100
    for i in range(-100, 101):
        if a == i**3 and (i**2 == -a or a == -i**2 and i%2 == 0):
            return True
    # check if a is the cube of a number between -100 and 100
    for i in range(-100, 101):
        if a == i**3 and (
