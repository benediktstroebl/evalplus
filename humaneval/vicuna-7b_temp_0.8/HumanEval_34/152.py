

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    if not l:
        return []
    elif not l[0]:
        return [l[1]]
    else:
        result = []
        for item in l:
            if item not in result:
                result.append(item)
        return result