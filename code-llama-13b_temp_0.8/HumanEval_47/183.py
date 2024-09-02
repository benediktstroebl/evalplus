

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    "*** YOUR CODE HERE ***"
    copy = l.copy()
    copy.sort()
    index = int(len(copy) / 2)
    if len(copy) % 2 != 0:
        return copy[index]
    else:
        return (copy[index] + copy[index-1]) / 2

