
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
    # 1st brute-force solution
    # return a in set([a**3 for a in range(a+1)])
    # return a in [x**3 for x in range(a+1)]
    # 2nd solution
    # return any(a % b == 0 for b in range(1, a+1) if a % b == 0)
    # 3rd solution
    return any(a % x == 0 for x in range(1, a+1) if a % x == 0)
