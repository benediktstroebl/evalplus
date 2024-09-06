

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    seen = set()
    result = sorted(l, reverse=True)
    for elt in result:
        if elt not in seen:
            seen.add(elt)
            result.remove(elt)
            result.insert(0, elt)
    return result