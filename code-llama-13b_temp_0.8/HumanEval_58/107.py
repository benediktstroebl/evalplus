

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1.sort()
    l2.sort()
    l1_len, l2_len = len(l1), len(l2)
    res = []

    i1, i2 = 0, 0
    while i1 < l1_len and i2 < l2_len:
        if l1[i1] == l2[i2]:
            res.append(l1[i1])
            i1 += 1
            i2 += 1
        elif l1[i1] > l2[i2]:
            i2 += 1
        else:
            i1 += 1

    return res

