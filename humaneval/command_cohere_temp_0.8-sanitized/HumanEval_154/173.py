def cycpattern_check(a, b):
    s = set(a)
    return b in s or any(x in a for x in s if x != b and x != a)