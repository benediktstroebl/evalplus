

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    res = []
    for val in l:
        if val not in res:
            res.append(val)
    return sorted(res)

results = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])

assert results == [0, 2, 3, 5, 9, 123], "Unique element list check failed"
