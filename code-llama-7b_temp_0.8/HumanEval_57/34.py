

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    increasing = True
    decreasing = True

    # If increasing is true, then check if the next item in the list is greater than the current.
    # If increasing is false, then check if the next item in the list is less than the current.
    # Do this until the end of the list.
    for i in range(len(l) - 1):
        if increasing and l[i + 1] < l[i]:
            increasing = False
        if decreasing and l[i + 1] > l[i]:
            decreasing = False
        if not increasing and not decreasing:
            return False

    return True

