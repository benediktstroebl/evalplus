def iscube(a):
    # Check if the number is positive
    if a <= 0:
        return False 
    elif a == 0:
        return True

    # Check if the number is an integer
    if a % 1:
        return False 
    elif a == 1:
        return True

    # Find the smallest integer b whose cube is a
    for b in range(1, int(a**(1/3)) + 1):
        if a == b**3:
            return True

    return False