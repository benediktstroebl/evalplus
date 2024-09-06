

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) == 0:
        return []
    if len(l2) == 0:
        return []

    if len(l1) == 1:
        return l2.count(l1[0])

    if len(l2) == 1:
        return l1.count(l2[0])

    for x in l1:
        if x in l2:
            return l2.remove(x)

    for x in l2:
        if x in l1:
            return l1.remove(x)

    return l1.union(l2)