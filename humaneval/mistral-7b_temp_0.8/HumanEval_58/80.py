

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if l1 == l2:
        return l1
    elif l1.sort() < l2.sort():
        for i in range(len(l1)):
            if l1[i] == l2[i]:
                return l1[i]
            elif l1[i] != l2[i]:
                return common(l1[i + 1:], l2[i + 1:])
    else:
        for i in range(len(l2)):
            if l1[i] == l2[i]:
                return l1[i]
            elif l1[i] != l2[i]:
                return common(l1[i + 1:], l2[i + 1:])

