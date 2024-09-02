

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    unique_elems = []
    for elem in l:
        if elem not in unique_elems:
            unique_elems.append(elem)
    return sorted(unique_elems)

