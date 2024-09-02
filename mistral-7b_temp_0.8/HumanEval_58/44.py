

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if l1 == [] or l2 == []:
        return []
    l1.sort()
    l2.sort()
    common = []
    l1_idx = 0
    l2_idx = 0
    while l1_idx < len(l1) and l2_idx < len(l2):
        if l1[l1_idx] == l2[l2_idx]:
            common.append(l1[l1_idx])
            l1_idx += 1
            l2_idx += 1
        elif l1[l1_idx] < l2[l2_idx]:
            l1_idx += 1
        else:
            l2_idx += 1

    return sorted(common)

