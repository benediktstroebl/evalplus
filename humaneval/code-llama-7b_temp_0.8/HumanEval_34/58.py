

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    new_list = []
    for i in range(len(l)):
        if l[i] not in new_list:
            new_list.append(l[i])
    new_list.sort()
    return new_list

