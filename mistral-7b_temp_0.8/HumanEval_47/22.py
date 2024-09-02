

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    """
    Important Notes:
    - Sort the list before finding the median,
    - 2nd and 3rd quartiles are median.
    - Odd number of items have single median value.
    - Even number of items have 2 median values.
    - If there is 1 item, then the median value is the item.
    """
    if len(l) == 0:
        raise ValueError('List must have at least 1 element')
    if len(l) % 2 == 0:
        return (l[int(len(l) / 2) - 1] + l[int(len(l) / 2)]) / 2
    return l[int(len(l) / 2)]

