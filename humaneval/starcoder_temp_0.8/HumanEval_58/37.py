

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l = []
    m1 = l1[:]
    m2 = l2[:]
    l1.sort()
    l2.sort()
    while m1 and m2:
        if m1[0] == m2[0]:
            l.append(m1.pop(0))
            m2.pop(0)
        elif m1[0] < m2[0]:
            m1.pop(0)
        else:
            m2.pop(0)
    return l
