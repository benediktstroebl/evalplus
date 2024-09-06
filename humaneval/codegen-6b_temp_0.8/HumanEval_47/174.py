

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError("Cannot divide the empty list.")
    sortedL = sorted(l)
    if len(sortedL) % 2 == 0:
        length = len(sortedL)
        return (sortedL[length // 2 - 1] + sortedL[length // 2]) / 2
    else:
        return sortedL[len(sortedL) // 2]
