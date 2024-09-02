

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    seen = {}
    result = sorted(list(filter(lambda x: x not in seen, l)))
    for x in result:
        seen[x] = 1
    return result
