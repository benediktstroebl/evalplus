

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if not l1:
        return l1
    if not l2:
        return l2
    p1, p2 = 0, 0
    res = []
    while 1:
        if p1 == len(l1) or p2 == len(l2):
            break
        if l1[p1] == l2[p2]:
            res.append(l1[p1])
            p1 += 1
            p2 += 1
        elif l1[p1] < l2[p2]:
            p1 += 1
        else:
            p2 += 1
    return res
