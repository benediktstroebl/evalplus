

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    s1 = sorted(l1)
    s2 = sorted(l2)
    i1 = i2 = 0
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] == s2[i2]:
            yield s1[i1]
            i1 += 1
            i2 += 1
        elif s1[i1] < s2[i2]:
            i1 += 1
        else:
            i2 += 1

