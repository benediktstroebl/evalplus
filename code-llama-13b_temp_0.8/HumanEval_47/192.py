

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # sort list and find the median index
    l.sort()
    index = len(l) // 2
    # if there is even number of elements
    # we should take the mean of two middle elements
    if len(l) % 2 == 0:
        median = (l[index - 1] + l[index]) / 2
    # if there is odd number of elements
    # the median is the middle element
    else:
        median = l[index]
    return median

