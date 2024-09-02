

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    if not l[0] < l[-1]:
        return l[-1]
    if len(l) % 2 == 1:
        # if odd length, return the middle
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        # if even length, return the average of the middle 2
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2

