def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    import math
    if a < 0:
        a = -a
    root = int(math.sqrt(a))
    exponent = root * root * root
    return a == exponent