

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)

    common_l = []
    i = 0
    j = 0

    while i < len(sorted_l1) and j < len(sorted_l2):
        if sorted_l1[i] == sorted_l2[j]:
            common_l.append(sorted_l1[i])
            i += 1
            j += 1
        elif sorted_l1[i] < sorted_l2[j]:
            i += 1
        else:
            j += 1

    return sorted(common_l)

