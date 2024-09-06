def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    # Assumption: input is always valid
    if a < 0:
        a = a * a * a
    return a ** (1/3) == int(a ** (1/3))