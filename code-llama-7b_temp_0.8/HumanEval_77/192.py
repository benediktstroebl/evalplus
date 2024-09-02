
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

    return (int(round(a**(1.0/3))))**3 == a
    
    '''
    def square(x):
        return x * x

    def iscube(a):
        # Return True if x is a perfect cube, else False.
        # Note: you may assume that x is an integer.
        if a < 0:
            return iscube(-x)
        x = a
        n = int(round(x**(1.0/3)))
        return n**3 == x
    '''
