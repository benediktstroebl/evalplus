def iscube(a):
    if a < 0:
        a = -a
    if a > 0:
        return a ** 3 == int(a ** 3)
    else:
        return a == int(a ** 3)