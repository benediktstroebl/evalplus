

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    n = len(l)
    if n == 0:
        return []
    elif n == 1:
        return [l[0]]
    else:
        return unique([l[0]] + unique([l[1:]]))
