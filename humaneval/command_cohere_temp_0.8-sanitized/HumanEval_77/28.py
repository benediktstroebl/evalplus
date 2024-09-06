def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    # Check the cube root of the integer a
    return a ** (1/3) == round(a ** (1/3))