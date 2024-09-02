

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    assert l, 'The list cannot be empty'
    # Sort the elements
    l.sort()
    # Keep track of even and odd counts
    odd = len(l) % 2
    if odd:
        return l[len(l) // 2]
    else:
        return float(l[(len(l) - 1) // 2] + l[(len(l) - 2) // 2]) / 2.0


