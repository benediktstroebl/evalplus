
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
    if a == 0:
        return True
    elif a % 1 == 0:
        return False
    elif a % 2 == 0:
        return iscube(a // 2)
    elif a % 3 == 0:
        return iscube(a // 3)
    elif a % 4 == 0:
        return iscube(a // 4)
    elif a % 5 == 0:
        return iscube(a // 5)
    elif a % 6 == 0:
        return iscube(a // 6)
    elif a % 7 == 0:
        return iscube(a // 7)
    elif a % 8 == 0:
        return iscube(a // 8)
    elif a % 9 == 0:
        return iscube(a // 9)
    elif a % 10 == 0:
        return iscube(a // 10)
    elif a % 11 == 0:
        return iscube(a // 11)
    elif a % 12 == 0:
        return iscube(a // 12)
    elif a % 13 == 0:
        return iscube(a // 13)
    elif a % 14 == 0:
        return iscube(a // 14)
    elif a % 15 == 0:
        return iscube(a // 15)
    elif a % 16 == 0:
        return iscube(a // 16)
    elif a % 17 == 0:
        return iscube(a // 17)
    elif a % 18 == 0:
        return iscube(a // 18)
    elif a % 19 == 0:
        return iscube(a // 19)
    elif a % 20 == 0:
        return iscube(a // 20)
    else:
        return False
