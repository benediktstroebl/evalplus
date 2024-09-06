def iscube(a):
    # Check if the number is divisible by 2 but not equal to 2
    if a > 2 and (a % 2 == 0) and (a != 2):
        return True
    # Check if the number is divisible by 3 but not equal to 3
    if a > 3 and (a % 3 == 0) and (a != 3):
        return True
    # Check if the number is divisible by 4 but not equal to 4
    if a > 4 and (a % 4 == 0) and (a != 4):
        return True
    # Check if the number is divisible by 5 but not equal to 5
    if a > 5 and (a % 5 == 0) and (a != 5):
        return True
    # Check if the number is divisible by 6 but not equal to 6
    if a > 6 and (a % 6 == 0) and (a != 6):
        return True
    # If none of the above, return False
    return False