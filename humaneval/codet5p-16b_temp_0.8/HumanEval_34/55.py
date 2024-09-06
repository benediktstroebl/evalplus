

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    if l is None or len(l) == 0:
        return []
    hash_list = {}
    return [hash_list.setdefault(x, x) for x in l]
