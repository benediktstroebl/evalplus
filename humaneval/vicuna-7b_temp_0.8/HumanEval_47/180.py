

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n % 2 == 0:
        return (sum(l) / n) / 2.0
    else:
        if n % 3 == 0:
            return (sum(l) // (n // 3) // 3)
        else:
            return (sum(l) // n) + (sum(l) // (n + 1)) / 2.0
