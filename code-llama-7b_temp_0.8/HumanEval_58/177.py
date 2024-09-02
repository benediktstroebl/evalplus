

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # new list of list
    l11 = sorted(l1)
    l22 = sorted(l2)
    i = 0
    j = 0
    result = []

    # cycle through the lists
    while i < len(l11) and j < len(l22):
        if l11[i] == l22[j]:
            if l11[i] not in result:
                result.append(l11[i])
            i += 1
            j += 1
        elif l11[i] > l22[j]:
            j += 1
        else:
            i += 1

    return sorted(result)

