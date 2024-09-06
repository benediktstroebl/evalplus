def cycpattern_check(a, b):
    s = set()
    for i in range(1, min(len(a), len(b)) + 1):
        if a[:i] in s:
            return True
        s.add(a[:i])
    return b in a or b[:len(a)] == a