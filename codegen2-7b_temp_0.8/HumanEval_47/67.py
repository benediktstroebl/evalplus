

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n < 1:
        raise ValueError('empty list')
    elif n == 1:
        return l[0]
    elif n % 2 == 0:
        return sum(l[n // 2 - 1:n // 2 + 1]) /
