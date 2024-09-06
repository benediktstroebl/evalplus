def is_sorted(lst):
    # Input Validation
    if not lst:
        return False
    if not all(isinstance(n, int) for n in lst):
        return False
    if lst[0] < 0:
        return False
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] != 1)