

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    common_elements = []
    for i in range(min(len(l1), len(l2))):
        if l1[i] in l2 and l1[i] not in common_elements:
            common_elements.append(l1[i])
        if l2[i] in l1 and l2[i] not in common_elements:
            common_elements.append(l2[i])

    return sorted(common_elements)

