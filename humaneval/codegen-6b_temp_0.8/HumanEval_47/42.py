

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    [print(l) for i in range(len(l))]
    num_of_elem = len(l)
    if num_of_elem % 2 == 0:
        median = (l[int((num_of_elem + 1) / 2 - 1)] + l[int((num_of_elem + 1) / 2)]) / 2
    else:
        median = l[int((num_of_elem + 1) / 2 - 1)]
    return median

