

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    if not l:
        return []
    else:
        l.sort()
        seen = set()
        return [x for x in l if x not in seen and x not in (0, 1)]