

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    if not l: return []
    res = [l[0]]
    for elem in l[1:]:
        if elem != res[-1]:
            res.append(elem)
    return res
