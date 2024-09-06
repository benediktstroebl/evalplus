

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    unique = []
    for elem in l:
        if elem not in unique:
            unique.append(elem)
    return sorted(unique)
