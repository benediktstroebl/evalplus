

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # Check edge case
    if len(l) == 0:
        raise ValueError("List must contain at least one element")

    # Make a copy of the original list, so that it doesn't mutate
    l = l[:]
    l.sort()

    if len(l) % 2 == 0:
        # If there are an even number of elements, return average of middle two
        median_index = len(l) // 2
        return (l[median_index - 1] + l[median_index]) / 2
    else:
        # If there are an odd number of elements, return the middle element
        return l[len(l) // 2]

