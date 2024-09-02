
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
    if a**3==int(a**3):
        return True
    else:
        return False

assert iscube(0)
assert iscube(1)
assert iscube(2) == False
assert iscube(3) == False
assert iscube(-1)
assert iscube(64)
assert iscube(360)
assert iscube(1000)
assert iscube(9999)
