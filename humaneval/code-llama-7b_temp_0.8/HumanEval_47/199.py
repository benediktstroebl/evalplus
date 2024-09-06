

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # The median is the middle element when the list has an even number of
    # elements. If the list has an odd number of elements, the middle
    # element is the one at the middle position

    if len(l) % 2 == 1:
        return l[len(l)//2]
    return (l[len(l)//2 - 1] + l[len(l)//2]) / 2.0

