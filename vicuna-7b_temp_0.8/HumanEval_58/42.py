

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    seen = set()
    for el1 in l1:
        if el1 not in seen:
            seen.add(el1)
            yield el1
    for el2 in l2:
        if el2 not in seen:
            seen.add(el2)
            yield el2
    for i in range(len(l1)):
        for j in range(len(l2)):
            if (l1[i] == l2[j]) and (l1[i] not in seen):
                yield l1[i]
    for i in range(len(l1)):
        if l1[i] not in seen:
            yield l1[i]

l1 = [1, 4, 3, 34, 653, 2, 5]
l2 = [5, 7, 1, 5, 9, 653, 121]
