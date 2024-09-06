def sort_third(l):
    return l[:] if not isinstance(l, list) else l[:] if len(l) % 3 else sorted([val for i, val in enumerate(l) if i % 3])