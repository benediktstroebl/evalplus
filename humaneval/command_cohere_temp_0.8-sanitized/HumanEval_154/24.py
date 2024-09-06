def cycpattern_check(a, b):
    a, b = a.lower(), b.lower()
    return any(b in s for s in a) or any(a == s[:len(a)] for s in b)