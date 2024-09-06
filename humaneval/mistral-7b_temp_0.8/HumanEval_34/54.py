

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Your code here
    l.sort()
    un = []
    for i in range(len(l)):
        if i == 0 or l[i] != l[i - 1]:
            un.append(l[i])
    return un

