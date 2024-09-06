def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    # Note: you may assume the input is always valid
    if a < 0:
        a = a * a * a
    else:
        a = a * a * a
        a = max(a, 1)
    return a == int(a ** (1/3))