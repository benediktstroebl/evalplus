

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    d1 = {}
    d2 = {}
    for e1, e2 in zip(l1, l2):
        if e1 in d1:
            d1[e1] += 1
        else:
            d1[e1] = 1
        if e2 in d2:
            d2[e2] += 1
        else:
            d2[e2] = 1
    return [k for k in d1.keys() if d1[k] > 0 and d2[k] > 0]
