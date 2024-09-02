

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # unsorted list of unique elements
    # unique = sorted(set(l))
    # return unique
    # sorted list of unique elements
    unique = []
    for item in l:
        if item not in unique:
            unique.append(item)
    return sorted(unique)

