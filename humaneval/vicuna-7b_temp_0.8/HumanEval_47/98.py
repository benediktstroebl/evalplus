

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # sort the list
    l = sorted(l)
    # check if the list is empty
    if len(l) == 0:
        return 0
    # compute the sum of the elements
    s = sum(l)
    # compute the median as the middle element plus half of the sum
    return (s/2.0 + l[len(l)//2]) / 2.0
