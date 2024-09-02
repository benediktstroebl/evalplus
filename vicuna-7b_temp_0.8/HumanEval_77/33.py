
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
    if a > 0:
        # if the number is positive, it is a cube if it is a power of 3
        return (a == 3**n for n in range(0, int(a**0.5) + 1))
    elif a < 0:
        # if the number is negative, it is a cube if it is a power of -3
        return (a == -3**n for n in range(0, int(-a**0.5) + 1))
    else:
        # if the number is zero, it is a cube if it is a power of 0
        return a == 0

a = int(input("Enter a number: "))
