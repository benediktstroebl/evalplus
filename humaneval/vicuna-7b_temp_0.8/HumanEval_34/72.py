

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    n = len(l)
    result = []
    while n > 0:
        # find unique elements
        unique_indices = [i for i, x in enumerate(l) if x not in result or i == 0]
        # add unique elements to result
        result.extend(unique_indices)
        # remove duplicates from the rest of the list
        l = l[1:]
        # update counter
        n -= len(unique_indices)
    return result
