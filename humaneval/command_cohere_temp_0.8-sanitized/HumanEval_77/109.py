def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    import math
    if a < 0:
        a = -a
    b = int(math.sqrt(a)) ** 3
    if a == b:
        return True
    else:
        return False