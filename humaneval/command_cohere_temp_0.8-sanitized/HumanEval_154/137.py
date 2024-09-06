def cycpattern_check(a, b):
    a = a.lower()
    b = b.lower()
    b = b.replace(' ','')
    return b in a or any(b in rotate for rotate in (a[1:], a[2:], a[3:], a[:-1], a[:-2], a[:-3]))