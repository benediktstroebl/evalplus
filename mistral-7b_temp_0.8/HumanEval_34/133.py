

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    s = set()
    r = []
    for x in l:
        if x not in s:
            s.add(x)
            r.append(x)
    return sorted(r)
