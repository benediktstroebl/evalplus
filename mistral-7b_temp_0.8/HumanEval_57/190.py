

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Check if the length of the list is 0 or 1
    if len(l) <= 1:
        return True

    # Check if the first two elements are not in the right order
    if l[0] > l[1]:
        return False

    # Check if the last two elements are not in the right order
    if l[-2] < l[-1]:
        return False

    # Otherwise, return True
    return True

