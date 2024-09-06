def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, v in list(dups.items()):
        if v > 1:
            return False
    return True