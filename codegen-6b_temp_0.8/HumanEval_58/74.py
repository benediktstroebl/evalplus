

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    d1 = {}
    d2 = {}
    for x in l1:
        if x not in d1:
            d1[x] = 1
        else:
            d1[x] += 1
    for x in l2:
        if x not in d2:
            d2[x] = 1
        else:
            d2[x] += 1
    l = []
    for x in d1:
        if x in d2:
            if d1[x] <= d2[x]:
                l.append(x)
            else:
                l.append(x)
    for x in l:
        if l.count(x) > 1:
            l.remove(x)
    return l
