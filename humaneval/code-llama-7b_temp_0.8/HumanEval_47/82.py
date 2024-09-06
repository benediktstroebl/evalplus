

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    assert len(l) > 0, "List must have at least one element."
    l.sort()
    median_index = len(l) // 2
    if len(l) % 2 == 1:
        return l[median_index]
    else:
        return (l[median_index - 1] + l[median_index]) / 2.0

