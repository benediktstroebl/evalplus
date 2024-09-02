

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    l.sort()
    return [e for i, e in enumerate(l) if i == 0 or e != l[i-1]]

