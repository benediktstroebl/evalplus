

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1.sort()
    l2.sort()
    p1, p2 = 0, 0
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]:
            p1 += 1
        elif l2[p2] < l1[p1]:
            p2 += 1
        else:
            yield l1[p1]
            p1 += 1
            p2 += 1
    return l1[p1:]

