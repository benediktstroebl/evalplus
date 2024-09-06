
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
    b=0
    c=0
    while a!=0:
        c+=1
        b=b*10
        a=a/10
    b=int(b)
    for i in range(c):
        b=b*10
        b=int(b)
    return a==b

