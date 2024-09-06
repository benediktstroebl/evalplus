

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # there are some inefficiencies in this algorithm
    # but it should be pretty clear what's going on
    # let me know if you want more of an explanation
    l = sorted(l)
    # need to be able to return a float for cases like [1, 2, 3, 4]
    if len(l) % 2 == 1:
        return l[(len(l) - 1) // 2]
    else:
        index = len(l) // 2
        return (l[index - 1] + l[index]) / 2.0

