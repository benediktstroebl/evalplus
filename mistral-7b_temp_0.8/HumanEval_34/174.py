

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    l_len = len(l)
    res = []

    for i in range(l_len):
        if l[i] not in res:
            res.append(l[i])

    return sorted(res)

