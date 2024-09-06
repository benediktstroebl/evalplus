def sort_third(l):
    l_copy = l.copy()
    return l_copy[:] + [x for i, x in enumerate(l) if i % 3 == 0 and l_copy[i] not in l[:i % 3 == 0]]