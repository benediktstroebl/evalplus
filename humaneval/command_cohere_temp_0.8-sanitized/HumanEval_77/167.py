def iscube(a):
    # Check if the number is divisible by 2 and then 3
    if a % 2 == 0 and a % 3 == 0:
        return True
    else:
        return False