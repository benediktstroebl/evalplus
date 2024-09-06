def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the smallest integer b whose cube is a
    for b in range(1, int(a**0.33333) + 1):
        if a == b**3:
            return True

    return False