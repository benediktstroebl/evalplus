

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(l) % 2 == 0:
        mid = len(l) // 2
        return sum(l[mid - i + 1] for i in range(mid, len(l))) / 2
    else:
        return (sum(l[i] for i in range(len(l) // 2 - 1)) + sum(l[i] for i in range(len(l) // 2, len(l)))) / 2