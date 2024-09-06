def sort_third(l):
    return l[:] if not isinstance(l, list) else l[:] if len(l) % 3 else l[:len(l) // 3 * 2] + sorted(l[len(l) // 3 * 2:])