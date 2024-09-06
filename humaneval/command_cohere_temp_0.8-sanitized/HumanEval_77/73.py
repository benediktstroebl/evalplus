def iscube(a):
    if a < 0:
        a = -a
    if a > 0 and a ** (1/3) == int(a ** (1/3)):
        return True
    else:
        return False