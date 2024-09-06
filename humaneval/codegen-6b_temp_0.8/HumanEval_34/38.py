

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    i = 0
    n = len(l)
    l2 = []
    while i < n:
        if l[i] not in l2:
            l2.append(l[i])
        i += 1
    return l2
