
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
        a = str(a)
        for i in range(len(a) - 1, -1, -1):
            if a[i] == '1':
                break
            elif a[i] != '0':
                return False
        return True
    else:
        for i in range(len(a) - 1, -1, -1):
            if a[i] == '1':
                break
            elif a[i] != '0':
                return False
        return True
