

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Your code here.
    # The purpose of this test is to ensure that the algorithm can perform a
    # comparison.
    if l[0] > l[-1]:
        return l[0]
    return l[-1]

