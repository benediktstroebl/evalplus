

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    if l == []:
        return []
    else:
        return unique(l[1:]) + unique(l[1:][l[0] < l[1]])

