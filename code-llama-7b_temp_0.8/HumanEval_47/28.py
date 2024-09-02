

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list first.
    l.sort()
    # Get the length of the list.
    n = len(l)
    # If the list is empty, return None.
    if n == 0:
        return None
    # If the list contains only one element, return that element.
    elif n == 1:
        return l[0]
    # If the list contains an even number of elements, get the two middle elements.
    # Then, return the average of those two elements.
    elif n % 2 == 0:
        i1 = n // 2 - 1
        i2 = n // 2
        return (l[i1] + l[i2]) / 2
    # If the list contains an odd number of elements, get the middle element.
    else:
        i = n // 2
        return l[i]

