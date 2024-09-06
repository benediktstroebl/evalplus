

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    seen = set()
    result = sorted(l, key=lambda x: x if x not in seen else len(seen) + 1)
    return [x for x in result if x not in seen]
