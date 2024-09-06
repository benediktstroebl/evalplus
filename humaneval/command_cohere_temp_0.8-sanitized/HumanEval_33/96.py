def sort_third(l):
    return l[:] if not l or len(l) % 3 else sorted([val for i, val in enumerate(l) if i % 3 == 0]) + l[::3]