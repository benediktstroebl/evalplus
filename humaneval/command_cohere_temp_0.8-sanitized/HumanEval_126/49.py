def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    for x in dups:
        if dups[x] > 1:
            return False
    return len(set(lst)) == len(lst) and all(lst[i] <= lst[i+1] for i in range(len(lst)-1))