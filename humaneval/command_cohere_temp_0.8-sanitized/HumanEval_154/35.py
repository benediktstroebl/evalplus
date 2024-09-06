def cycpattern_check(a, b):
    a = a.lower()
    b = b.lower()
    return b in a or any(b in rotatedWord for rotatedWord in a.rotate(-1))