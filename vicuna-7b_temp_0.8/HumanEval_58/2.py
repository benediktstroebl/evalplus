

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    if len(l1) == 0 or len(l2) == 0:
        return []

    if len(l1) < len(l2):
        l2 = sorted(l2)
    else:
        l1 = sorted(l1)

    seen = set()

    for x in l1:
        if x in seen or x in l2:
            continue
        seen.add(x)
        yield x

        for y in l2:
            if y == x or y in seen:
                continue
            seen.add(y)
            yield y
