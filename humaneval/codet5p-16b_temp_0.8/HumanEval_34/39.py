

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    
    if len(l) == 1:
        return [l[0]]
    
    unique_l = []
    for i in l:
        if i not in unique_l:
            unique_l.append(i)
    return unique_l
