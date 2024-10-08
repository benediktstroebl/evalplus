

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1 = list(set(l1))
    l2 = list(set(l2))
    l1.sort()
    l2.sort()
    result = []
    while l1 and l2:
        if l1[0] == l2[0]:
            result.append(l1[0])
            l1.pop(0)
            l2.pop(0)
        elif l1[0] < l2[0]:
            l1.pop(0)
        elif l1[0] > l2[0]:
            l2.pop(0)
    return result

