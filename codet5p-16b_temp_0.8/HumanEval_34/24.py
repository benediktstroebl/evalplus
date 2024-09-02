

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    if not l:
        return []
    elif len(l) == 1:
        return l

    if l[0] < l[1]:
        head = l[0]
        tail = l[1:]
    else:
        head = l[1]
        tail = l[:1]

    return unique(tail) + [head]

