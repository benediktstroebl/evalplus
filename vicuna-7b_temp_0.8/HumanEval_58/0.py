

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if not l1 and not l2:
        return []
    if not l1 or not l2:
        return [None]
    if len(l1) != len(l2):
        return [None]

    unique1 = set(l1)
    unique2 = set(l2)
    intersection = unique1.intersection(unique2)
    result = []
    for num in intersection:
        if num not in unique1 or num not in unique2:
            result.append(num)
    return result