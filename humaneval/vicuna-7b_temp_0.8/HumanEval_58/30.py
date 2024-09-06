

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) < len(l2):
        l1 = sorted(l1, reverse=True)
    if len(l1) < len(l2):
        l2 = sorted(l2, reverse=True)
    return [x for x in set(l1).intersection(l2) if x not in set(l1) and x not in set(l2) and x not in l1 and x not in l2]
