def sort_third(l):
    return l[:] if not l or len(l) % 3 else sorted(l[i] for i in range(0, len(l), 3))