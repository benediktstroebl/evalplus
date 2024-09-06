

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    a = l.copy()
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                a.pop(j)
    return a
