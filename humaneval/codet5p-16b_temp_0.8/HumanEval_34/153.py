

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    if len(l) == 0:
        return []
    unique = [l[0]]
    for x in l:
        if x not in unique:
            unique.append(x)
    return sorted(unique)
