

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    l.sort()
    unique_l = [l[0]]
    for i in l[1:]:
        if i!= unique_l[-1]:
            unique_l.append(i)
    return unique_
