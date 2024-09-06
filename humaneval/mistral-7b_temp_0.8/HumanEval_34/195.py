

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # list of all seen values
    seen = []

    # all sorted list
    l_sorted = sorted(l)

    # if seen is empty, then l_sorted is unique
    if not seen:
        return l_sorted

    for value in l_sorted:
        # if value is not seen, then add value to seen list
        if value not in seen:
            seen.append(value)

    return seen
