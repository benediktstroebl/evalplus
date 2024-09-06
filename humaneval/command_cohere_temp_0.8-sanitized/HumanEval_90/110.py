def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    mn, mx = min(lst), max(lst)
    sm = mn
    for v in lst:
        if v == mx:
            continue
        if v == sm:
            sm = mn
        elif v < sm:
            sm = v
    return sm