

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    if not l:
        return []
    e = l[0]
    return [e] if all(e == x for x in l) else unique(l[1:]) + [e]
