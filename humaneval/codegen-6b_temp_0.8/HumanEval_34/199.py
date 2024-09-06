

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    l.sort()
    # remove duplicates
    results = []
    last = None
    for el in l:
        if el != last:
            results.append(el)
            last = el
    return results

