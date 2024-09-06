

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    n = len(l)
    if n == 0:
        return []
    u = []
    for i in range(n):
        if i == 0 or l[i] != l[i - 1]:
            u.append(l[i])
    return u
