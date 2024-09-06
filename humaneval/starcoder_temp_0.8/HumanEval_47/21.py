

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l_sorted = sorted(l)
    length = len(l)
    if length % 2 == 1:
        return l_sorted[int((length-1)/2)]
    else:
        i = int(length/2)
        return (l_sorted[i] + l_sorted[i-1])/2.0

