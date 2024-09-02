

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    result = []
    if len(l1) > len(l2):
        temp = l2
        l2 = l1
        l1 = temp

    for element in l1:
        if element in l2:
            result.append(element)
            l2.remove(element)

    return sorted(result)
