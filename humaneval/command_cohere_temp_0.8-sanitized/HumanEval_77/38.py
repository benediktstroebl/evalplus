def iscube(a):
    if a < 0:
        a = -a
    elif a == 0:
        return True
    else:
        for i in range(1, a):
            if a % i == 0 and a // i == i:
                return True
    return False