def sort_third(l):
    return l[:] if not isinstance(l, list) else l[:] if not len(l) else [el if i % 3 != 0 else sorted( [el for el in l if el == li])[0] for i, li in enumerate(l)]