

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    len_list = len(l)
    median = 0
    if len_list % 2 == 0:
        index_median = (len_list-1)//2
        median = (l[index_median] + l[index_median + 1])/2
    else:
        median = l[len(l)//2]
    return median
