

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    u = {}
    for e in l:
        u[e] = 1
    lu = [e for e in u]
    lu.sort()
    return lu

