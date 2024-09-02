

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) == 0:
        return []
    if len(l2) == 0:
        return []
    if len(l1) == 1:
        return l1

    l1 = sorted(l1)
    l2 = sorted(l2)
    result = []
    for i in range(len(l1)):
        if l1[i] in l2:
            result.append(l1[i])
            if i + 1 == len(l1):
                break
    for i in range(len(l2), len(l1)):
        result.append(l2[i])

    return result
