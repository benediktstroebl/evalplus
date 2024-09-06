def next_smallest(lst):
    if len(lst) < 2:
        return None
    mn, mx = min(lst), max(lst)
    sm = mn
    for n in lst:
        if n > mx:
            continue
        if n > sm and n != mx:
            sm = n
    return sm