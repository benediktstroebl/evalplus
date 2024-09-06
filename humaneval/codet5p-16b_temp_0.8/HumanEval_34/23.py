

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    d = {}
    for x in l:
        d[x] = d.get(x, 0) + 1

    return sorted(d.keys())

