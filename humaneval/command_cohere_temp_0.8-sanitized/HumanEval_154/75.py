def cycpattern_check(a, b):
    a = a.lower()
    b = b.lower()
    return b in a or any(b[i:] + b[:i] in a for i in range(len(b) - 1))