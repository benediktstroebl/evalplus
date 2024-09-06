
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
    # 检查a是否为0
    if a == 0:
        return True
    # 如果a为负数，则返回False
    elif a < 0:
        return False
    # 检查a是否为1的倍数
    elif a % 1 == 0:
        return True
    # 如果a不是1的倍数，则返回False
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return True
        return False
