

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)
    if sorted_l1 == sorted_l2:
        return sorted_l1
    elif len(sorted_l1) > len(sorted_l2):
        i = 0
        while i < len(sorted_l1) - 1:
            if sorted_l1[i] != sorted_l2[i]:
                return [sorted_l1[i]]
            i += 1
        return [sorted_l1[i]]
    else:
        i = 0
        while i < len(sorted_l2) - 1:
            if sorted_l1[i] != sorted_l2[i]:
                return [sorted_l2[i]]
            i += 1
        return [sorted_l2[i]]

