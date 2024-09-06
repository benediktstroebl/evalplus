

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    n = len(l)
    new = []
    for i in range(n):
        if l[i] not in new:
            new.append(l[i])
    return sorted(new)

