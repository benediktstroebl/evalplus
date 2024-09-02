

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # YOUR CODE HERE
    sorted_l = sorted(l)
    unique_l = []
    for i in sorted_l:
        if i not in unique_l:
            unique_l.append(i)
    return unique_l

