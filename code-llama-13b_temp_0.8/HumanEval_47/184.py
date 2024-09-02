

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    "*** YOUR CODE HERE ***"
    copy = sorted(l)
    length = len(copy)
    if length % 2 == 0:
        return (copy[int(length/2)] + copy[int(length/2) - 1])/2
    else:
        return copy[int(length/2)]



































