

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1.sort()
    l2.sort()
    t = []
    i_1 = i_2 = 0
    while i_1 < len(l1) and i_2 < len(l2):
        if l1[i_1] == l2[i_2]:
            t.append(l1[i_1])
            i_1 += 1
            i_2 += 1
        elif l1[i_1] < l2[i_2]:
            i_1 += 1
        else:
            i_2 += 1

    return t
