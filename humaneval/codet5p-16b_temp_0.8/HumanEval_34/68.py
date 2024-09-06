

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    n = len(l)
    a = 0
    b = 1
    if n == 0:
        return []
    elif n == 1:
        return [l[0]]
    while b < n:
        if l[a]!= l[b]:
            a += 1
            l[a] = l[b]
        b += 1
    return l[:a+1]
