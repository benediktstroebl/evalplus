

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    "*** YOUR CODE HERE ***"
    l.sort()
    size = len(l)
    if size % 2 == 0:
        mid_idx = size//2
        return (l[mid_idx - 1] + l[mid_idx]) / 2
    else:
        return l[size//2]

