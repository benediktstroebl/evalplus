

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
        return [x for x in l2 if x not in l2]
    if not l2 or not l1:
        return [x for x in l1 if x not in l1]

    set1 = set(l1)
    set2 = set(l2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    result = sorted(intersection)
    for x in union:
        if x not in result:
            result.append(x)
    return result
