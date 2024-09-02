

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) == 0 or len(l2) == 0:
        return []
    elif len(set(l1).union(l2)) < len(l1) + len(l2):
        return []

    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            i += 1
        elif l2[j] <= l1[i]:
            j += 1
        else:
            return []

    return list(set(l1).union(l2))
