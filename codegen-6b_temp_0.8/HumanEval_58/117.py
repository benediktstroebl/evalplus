

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1.sort()
    l2.sort()
    res = []
    common = []
    common_p1 = 0
    common_p2 = 0
    while common_p1 < len(l1) and common_p2 < len(l2):
        if l1[common_p1] == l2[common_p2]:
            if common[common_p2] is None:
                common.append(l1[common_p1])
            common_p1 += 1
            common_p2 += 1
        elif l1[common_p1] < l2[common_p2]:
            common_p1 += 1
        else:
            common_p2 += 1
    return common


__author__ = 'frank'
