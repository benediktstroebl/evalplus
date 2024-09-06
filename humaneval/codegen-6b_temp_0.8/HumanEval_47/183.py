

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sortedlist = sorted(l)
    if len(sortedlist) % 2 == 0:
        return (sortedlist[len(sortedlist) // 2 - 1] + sortedlist[len(sortedlist) // 2]) / 2
    else:
        return sortedlist[len(sortedlist) // 2]
