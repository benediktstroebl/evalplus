
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
    if a < 0:
        return True
    if a in (0, 1):
        return True
    if a == 2:
        return True
    if a % 2 == 0:
        for i in range(3, int(a ** 0.5) + 1, 2):
            if a % i == 0:
                return True
        return False
    if a % 3 == 0:
        if a % 27 == 0:
            return True
        for i in range(3, int(a ** 0.5) + 1, 2):
            if a % i == 0:
                return True
        return False
    if a % 2 != 0:
        for i in range(1, int(a ** 0.5) + 1, 2):
            if a % i == 0:
                return True
        return False

a = int(input("Enter an integer: "))
result = iscube(a)
