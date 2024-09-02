

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # Make sure l is not empty
    if len(l) == 0:
        return True

    # Make sure l is not a single value
    if len(l) == 1:
        return True

    # Get the initial sign, True is increasing, False is decreasing
    sign = l[0] >= 0

    # Loop through the list
    for i in range(1, len(l)):
        # If the sign of the current element is different from the initial one, return False
        if sign != (l[i] >= 0):
            return False
        # If the current element is less than the previous one, return False
        if l[i] < l[i - 1]:
            return False

    # If we reach this point, all elements are increasing or decreasing, return True
    return True

