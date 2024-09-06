def iscube(a):
    if a < 0:
        a = -a
    elif a == 0:
        return True
    while a % 3 == 0:
        a /= 3
    return a == 1