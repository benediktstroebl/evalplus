

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # uniq, sort and use lower bound
    l1_uniq = sorted(set(l1))
    l2_uniq = sorted(set(l2))
    res = []
    i, j = 0, 0
    while i < len(l1_uniq) and j < len(l2_uniq):
        if l1_uniq[i] == l2_uniq[j]:
            res.append(l1_uniq[i])
            i += 1
            j += 1
        elif l1_uniq[i] < l2_uniq[j]:
            i += 1
        else:
            j += 1
    return res

