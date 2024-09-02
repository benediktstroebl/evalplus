

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    res = []
    if not l1 or not l2:
        return res
    # indexes for set l1
    i = 0
    # indexes for set l2
    j = 0
    while i < len(l1) and j < len(l2):
        # compare the elements
        if l1[i] == l2[j]:
            res.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    return sorted(set(res))

