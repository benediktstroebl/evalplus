def iscube(a):
    # Check if the number is divisible by 2 and itself at the same time
    if a % 2 == 0 and a ** (1/3) == int(a ** (1/3)):
        return True
    # If the number is not divisible by 2, then it must be a prime number
    elif a == 1 or a % 2 != 0:
        return a ** 3 == int(a ** 3)
    else:
        return False