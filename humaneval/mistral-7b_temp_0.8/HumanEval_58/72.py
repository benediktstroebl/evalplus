

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) > len(l2):
        return common(l2, l1)
    m = len(l1)
    i = 0
    for x in l2:
        if x not in l1:
            continue
        if i >= m:
            break
        if l1[i] == x:
            i += 1
            continue
        else:
            continue
    return sorted(l1[0:i])


