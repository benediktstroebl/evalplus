

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n % 2 == 0:
        return (n // 2) + 1
    else:
        #  odd number of elements
        k = (n + 1) // 2
        x = (n + 1) // 2
        if l[k] == l[x]:
            return (l[k] + l[x]) / 2
        else:
            return l[k]
