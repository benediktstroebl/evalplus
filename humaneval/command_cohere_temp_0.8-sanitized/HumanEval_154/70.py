def cycpattern_check(a, b):
    s = set()
    s.add(a)
    s.add(b)
    for i in range(len(b)):
        s.add(b[i:] + b[:i])
    return b in s and b != a