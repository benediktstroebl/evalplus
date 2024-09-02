

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    N: int = len(l)
    if N % 2 == 0:
        return (l[(N - 1) // 2] + l[(N + 1) // 2]) / 2
    else:
        center = (N - 1) // 2
        return l[center]

