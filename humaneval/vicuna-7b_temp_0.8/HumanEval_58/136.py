

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if not l1 or not l2:
        return []
    if len(l1) != len(l2):
        return []
    seen = set()
    result = []
    for x in l1:
        if x not in seen and x not in l2:
            seen.add(x)
            result.append(x)
    for y in l2:
        if y not in seen:
            seen.add(y)
            result.append(y)
    return result
