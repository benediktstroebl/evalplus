

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = sorted(l1)
    l2 = sorted(l2)
    l1_pos = 0
    l2_pos = 0
    len1 = len(l1)
    len2 = len(l2)
    result = []
    while l1_pos < len1 and l2_pos < len2:
        if l1[l1_pos] == l2[l2_pos]:
            result.append(l1[l1_pos])
            l1_pos += 1
            l2_pos +=
