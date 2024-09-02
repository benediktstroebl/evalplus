

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Test the first element with the second element
    if l[0] > l[1]:
        return False
    if l[0] < l[1]:
        return True

    # If we make it here, we can assume the first two elements are equal
    # Test the third element with the second element
    if l[2] > l[1]:
        return False
    if l[2] < l[1]:
        return True

    # If we make it here, we can assume the first three elements are equal
    # Test the fourth element with the second element
    if l[3] > l[1]:
        return False
    if l[3] < l[1]:
        return True

    # If we make it here, we can assume the first four elements are equal
    # Test the fifth element with the second element
    if l[4] > l[1]:
        return False
    if l[4] < l[1]:
        return True

    # If we make it here, we can assume the first five elements are equal
    # Test the sixth element with the
