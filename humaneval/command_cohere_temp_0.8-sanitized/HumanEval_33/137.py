def sort_third(l):
    return l[:] * (len(l) // 3) + sorted(l)[len(l) // 3:][:len(l) // 3]