def cycpattern_check(a, b):
    a, b = a.lower(), b.lower()
    return any(b in rot for rot in (a, a[1:] + a[:1], a[2:] + a[:2], a[3:] + a[:3],))