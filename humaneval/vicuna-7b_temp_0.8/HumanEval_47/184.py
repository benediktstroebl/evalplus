

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Use a heap to find the middle element
    l.heapify()
    # Find the middle element
    low, high = l.pop(0), l.pop(0)
    middle = (low + high) // 2
    # If the middle element is less than the median of the input list,
    # use the average of the last two elements as the new median
    if middle < l[len(l) // 2]:
        n = len(l) // 2
        return (l[n - 1] + l[n]) / 2
    # If the middle element is greater than the median of the input list,
    # use the middle element as the new median
    else:
        return middle