

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    if len(l) == 0:
        return l

    unique_list = []
    for i in range(len(l)):
        if l[i] not in unique_list:
            unique_list.append(l[i])

    return sorted(unique_list)

