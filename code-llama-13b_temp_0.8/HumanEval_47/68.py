

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # sort the list
    l.sort()

    # get the length of the list
    length = len(l)

    # if the list has an odd number of items, return the middle item
    if length % 2 == 1:
        return l[int(length / 2)]

    # if the list has an even number of items, return the average of the middle two items
    else:
        return (l[int(length / 2)] + l[int(length / 2) - 1]) / 2

