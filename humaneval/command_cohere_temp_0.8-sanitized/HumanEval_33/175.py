def sort_third(l):
    return l[:] if not isinstance(l, list) else l[:] if not l else [val for ind, val in enumerate(l) if ind % 3 != 0] + [sorted(l[ind] for ind, val in enumerate(l) if ind % 3 == 0)]