

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    i = 0
    j = 0
    for elm1, elm2 in zip(l1, l2):
        if elm1 < elm2:
            i += 1
        elif elm1 > elm2:
            j += 1
        else:
            return [elm1]
    return [elm for i in range(j) if i <= len(l1) and l1[i] == elm]
