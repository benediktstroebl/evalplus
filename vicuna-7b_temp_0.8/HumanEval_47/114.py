

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) % 2 == 0:
        n = len(l) // 2
        return sum(l[n-i+1:n]) / 2 for i in range(1, len(l))
    else:
        return sum(l[i:i+2]) / 2 for i in range(0, len(l)-1)
