def iscube(a):
    # Check if the number is greater than 0 and equals to cube of some integer
    return a > 0 and a ** (1/3) == int(a ** (1/3))