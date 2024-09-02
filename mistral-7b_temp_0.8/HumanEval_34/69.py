

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    sorted_unique_elements = []
    for item in l:
        if not item in sorted_unique_elements:
            sorted_unique_elements.append(item)
    return sorted(sorted_unique_elements)

