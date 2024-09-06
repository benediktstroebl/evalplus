

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if not l1:
        return l2
    if not l2:
        return l1
    i, j = 0, 0
    res = []
    while True:
        if l1[i] == l2[j]:
            res.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        if i == len(l1) or j == len(l2):
            break
    return res
