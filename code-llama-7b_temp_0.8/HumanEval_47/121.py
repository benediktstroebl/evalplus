

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # sort the list
    l.sort()

    # find the length of the list
    list_length = len(l)

    # find the middle element
    middle_index = list_length // 2

    # if the list length is odd, the median is the middle element
    if list_length % 2 != 0:
        median = l[middle_index]
    # if the list length is even, the median is the average of the two middle elements
    else:
        median = (l[middle_index] + l[middle_index - 1]) / 2
    return median

