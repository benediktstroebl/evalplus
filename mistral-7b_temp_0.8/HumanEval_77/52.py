
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
    # TODO: Write your solution below
    result = True if a == 0 or a % (a ** 0.5) == 0 else False
    return result
    # or
    # return a**0.5 == a**0.5.is_integer()
    # or
    # return a**0.5.is_integer()
    # or
    # return a**0.5 == int(a**0.5)
    # or
    # return a**0.5 == a**0.5 - int(a**0.5) == 0
