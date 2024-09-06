

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1.sort(); l2.sort()
    result = []; index1 = index2 = 0
    while index1 < len(l1) and index2 < len(l2):
        if l1[index1] == l2[index2]:
            result.append(l1[index1])
            index1 += 1; index2 += 1
        elif l1[index1] > l2[index2]:
            index2 += 1
        else:
            index1 += 1
    return result

