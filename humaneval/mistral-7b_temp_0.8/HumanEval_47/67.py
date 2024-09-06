

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # The `if` statement below is checking if the length of the list l is odd or even.
    # If the length is odd, the median is the middle element.
    if len(l) % 2 == 0:
        # The `middle` variable is set to the average of the two middle elements.
        middle = (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        # If the length is odd, the median is the middle element.
        middle = l[len(l) // 2]
    return middle

