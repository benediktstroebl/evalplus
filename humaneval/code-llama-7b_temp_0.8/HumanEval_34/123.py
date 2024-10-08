

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    new_l = []
    for x in l:
        if x not in new_l:
            new_l.append(x)
    return sorted(new_l)

