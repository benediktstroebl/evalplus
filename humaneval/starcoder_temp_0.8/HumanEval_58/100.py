

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    result = []
    l1.sort()
    l2.sort()
    a = 0
    b = 0
    while a < len(l1) and b < len(l2):
        if l1[a] == l2[b]:
            result.append(l1[a])
            a += 1
            b += 1
        elif l1[a] < l2[b]:
            a += 1
        else:
            b += 1
    return result
