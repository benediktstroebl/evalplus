

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    uniq, index = [], -1
    for i in l:
        index = (index + 1) % 2
        if index == 0 or i not in uniq:
            uniq.append(i)
    return uniq
