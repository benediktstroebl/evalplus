

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) == 0 or len(l2) == 0:
        return []
    elif len(l1) == 1 and l1[0] in l2:
        return [l1[0]]
    elif len(l2) == 1 and l2[0] in l1:
        return [l2[0]]
    else:
        return sorted(set(l1).union(l2))
