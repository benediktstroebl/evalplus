

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) > len(l2):
        l1, l2 = l2, l1
    s1 = sorted(l1)
    s2 = sorted(l2)
    res = []
    while s1 and s2:
        if s1[0] == s2[0]:
            res.append(s1.pop(0))
            s2.pop(0)
        elif s1[0] < s2[0]:
            res.append(s1.pop(0))
            s1.pop(0)
        else:
            res.append(s2.pop(0))
            s2.pop(0)
    return res
