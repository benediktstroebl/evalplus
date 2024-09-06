

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # iterate over list, keeping a record of monotonically increasing,
    # then check for monotonically decreasing
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            # next number is more, so check is increasing
            return False
        elif l[i] < l[i - 1]:
            # next number is less, so check is decreasing
            return True
    # well, if loop completes, we've gone as far as we can go, so the list
    # was monotonically increasing or decreasing
    return True
