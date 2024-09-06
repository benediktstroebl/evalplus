def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    # Note: you may assume the input is always valid
    if a < 0:
        a = abs(a)
    rev = int(str(a)[::-1])
    return rev ** 3 == a