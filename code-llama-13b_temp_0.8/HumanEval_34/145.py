

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    if len(l) < 2:
        return l
    l.sort()
    return [x for x, y in zip(l, l[1:]) if x != y] + [l[-1]]

