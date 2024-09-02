

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    l_len = len(l)
    if l_len % 2 == 1:
        # if odd number of elements in list,
        # return middle element
        return l[l_len // 2]
    else:
        # if even number of elements in list,
        # return average of the two middle elements
        return (l[l_len // 2] + l[l_len // 2 - 1]) / 2

