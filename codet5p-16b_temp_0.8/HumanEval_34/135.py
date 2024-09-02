

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    if not l:
        return []

    elements = {}
    for element in l:
        if element not in elements:
            elements[element] = True

    return [element for element in l if element in elements]
