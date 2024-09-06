

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    n = 0
    result = []
    for e in l:
        if e not in result or result[-1] < e:
            result.append(e)
            n += 1
    return result[n:]