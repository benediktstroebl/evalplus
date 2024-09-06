
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
    # If a is a cube of some integer n, then (a^2)^2 = a^3 = n^3.
    # Therefore, a^2 must be a square number.
    if a**2 == a*a:
        return True
    else:
        return False

a = int(input("Enter an integer: "))
