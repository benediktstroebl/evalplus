

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # s = sorted(set(l))
    # return s
    # return [s for s in l if l.count(s) == 1]
    return list(set(l))
