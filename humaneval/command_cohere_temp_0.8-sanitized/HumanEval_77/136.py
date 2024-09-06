def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)