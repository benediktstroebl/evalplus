

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    v = len(l) // 2
    return l[v] if len(l) % 2 else (l[v-1] + l[v])/2
