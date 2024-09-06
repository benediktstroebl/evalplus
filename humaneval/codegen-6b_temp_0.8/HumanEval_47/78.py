

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list
    l.sort()
    n = len(l)
    # If even number of elements, return the middle element
    if n % 2 == 0:
        return l[n/2]
    # If odd, return the average of the two middle elements
    else:
        return (l[n/2] + l[n/2 - 1]) / 2
   

