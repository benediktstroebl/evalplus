

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    result = []
    i1 = j1 = 0
    for i2 in range(len(l2)):
        if i1 == len(l1) or l1[i1] != l2[i2]:
            if j1 == len(l1) or l1[j1] != l2[i2]:
                result.append(l1[i1])
                i1 = j1 = 0
            else:
                result.append(l2[i2])
                j1 = i1 = 0
    if i1 < len(l1):
        result.append(l1[i1])
    return result