

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    assert len(l) >= 1
    n = len(l)
    half = n // 2
    l.sort()
    if n % 2 == 0:
        return (l[half - 1] + l[half]) / 2
    else:
        return l[half]

import doctest
doctest.testmod()
