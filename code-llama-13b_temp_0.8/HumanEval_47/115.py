

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    "*** YOUR CODE HERE ***"
    l.sort()
    n = len(l)
    if n % 2 == 0:
        a = l[n//2 - 1]
        b = l[n//2]
        median = (a + b)/2
        return median
    else:
        return l[n//2]

