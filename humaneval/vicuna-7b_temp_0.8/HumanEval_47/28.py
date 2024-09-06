

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n % 2 == 0:
        return (sum(l) / n) * 2
    else:
        n = n - 1
        x = sum(l) / n
        return x + (x * (n % 2))
