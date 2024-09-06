

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    if len(l1) == 0 or len(l2) == 0:
        return []

    l1.sort()
    l2.sort()

    i = 0
    j = 0

    results = []

    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            if len(results) == 0 or results[-1] != l1[i]:
                results.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1

    return results
