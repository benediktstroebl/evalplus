

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    print('solution 1')
    # using set
    s1 = set(l1)
    s2 = set(l2)
    return sorted(s1.intersection(s2))

    # Solution 2
    # using sorted list
    l1 = sorted(l1)
    l2 = sorted(l2)
    i = 0
    j = 0
    result = []
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            result.append(l1[i])
            i += 1
            j += 1
        else:
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
    return result

