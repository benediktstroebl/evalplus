
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
    # 最小值为0，最大值为abs(a)的最小整数平方根
    left = 0
    right = int(abs(a) ** (1/2))
    while left <= right:
        mid = (left + right) // 2
        if mid ** 3 == abs(a):
            return True
        elif mid ** 3 < abs(a):
            left = mid + 1
        else:
            right = mid - 1
    return False
