

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l_copy = sorted(l)
    length = len(l_copy)

    if length % 2 == 0:
        index_1 = length//2
        index_2 = index_1-1
        return (l_copy[index_1] + l_copy[index_2])/2
    else:
        return l_copy[length//2]

