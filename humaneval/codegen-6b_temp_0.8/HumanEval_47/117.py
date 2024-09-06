

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # http://stackoverflow.com/questions/24101524/finding-the-median-in-a-list-in-python
    # http://stackoverflow.com/questions/973194/finding-the-median-out-of-list-in-python
    # http://stackoverflow.com/questions/24101524/finding-the-median-in-a-list-in-python
    l.sort()
    return (l[(len(l) - 1) // 2] + l[len(l) // 2]) / 2.0
