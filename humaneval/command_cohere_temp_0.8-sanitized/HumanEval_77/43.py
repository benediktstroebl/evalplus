def iscube(a):
    if a == 0:
        return True
    elif a < 0:
        a = -a
    return a ** 3 == int(a ** 3)