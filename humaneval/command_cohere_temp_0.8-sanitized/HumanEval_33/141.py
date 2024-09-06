def sort_third(l):
    return l[:] if not isinstance(l, list) else [y for i, y in enumerate(l) if i % 3 != 0] + [sorted(x for x in l if i % 3 == 0)]