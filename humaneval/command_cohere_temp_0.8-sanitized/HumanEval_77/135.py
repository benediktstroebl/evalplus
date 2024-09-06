def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Find the largest cube that is less than or equal to a
    max_cube = int(pow(a ** (1/3)), 3)
    
    # If the largest cube is equal to a, return True
    if max_cube == a:
        return True
    return False