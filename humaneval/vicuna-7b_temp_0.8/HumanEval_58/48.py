

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) == 0 or len(l2) == 0:
        return []

    d1 = {}
    d2 = {}
    for item in l1:
        if item not in d1:
            d1[item] = 1
        else:
            d1[item] += 1

    for item in l2:
        if item not in d2:
            d2[item] = 1
        else:
            d2[item] += 1

    num = len(d1)
    for k in list(d2.keys()):
        if d1[k] > d2[k] - num:
            yield k
            while True:
                yield from l2[k]

    while True:
        yield from l1[list(d2.keys()).sort()[0]]
        while True:
            yield from l2[list(d2.values()).sort()[0]]

    for k in list(d1.keys()):
        if d2[k] > d1[k] - num:
            yield k
            while True:
                yield from l1[k]

    while True:
        yield from l2[list(d1.values()).sort()[0]]
        while True:
            yield from l1[list(d1.values()).sort()[0]]
