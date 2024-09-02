

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    if l == []:
        return l

    if l == [[]]:
        return l

    if l[0] == l[1]:
        return unique(l[2:])

    if l[0] == l[-1]:
        return unique(l[1:-1])

    return l[0] + unique(l[1:])

