def sort_third(l):
    return l[:] if not l or not isinstance(l, list) else l[:1] + sort_third(l[1:]) + [l[-1]] if l[-1] == sorted(l)[-1] else sort_third(l[:-1]) + [l[-1]]