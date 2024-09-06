def iscube(a):
    # Check if the number is divisible by 2 and leaves a remainder of 0, 
    # then it must be divisible by 2 again and leaves a remainder of 0 again
    if a % 2 == 0 and a**3 % 2 != 0:
        return False
    # Check if the number is divisible by 3 and leaves a remainder of 0, 
    # then it must be divisible by 3 again and leaves a remainder of 0 again
    if a % 3 == 0 and a**3 % 3 != 0:
        return False
    # Check if the number is divisible by 4 and leaves a remainder of 0, 
    # then it must be divisible by 4 again and leaves a remainder of 0 again
    if a % 4 == 0 and a**3 % 4 != 0:
        return False
    # If passed all conditions, then the number is a cube of some integer
    return True