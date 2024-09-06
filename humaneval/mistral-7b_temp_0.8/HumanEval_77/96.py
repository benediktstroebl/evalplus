
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
    if a<0:
        a = -a
    if a==1:
        return True
    if a%1!=0:
        return False
    for i in range(1,int(a**0.3+1)):
        if i*i*i==a:
            return True
    return False
