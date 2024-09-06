def iscube(a):
    if a < 0:
        a = -a
    if a == 0 or a == 1:
        return True
    return (a**3) % 6 == 0