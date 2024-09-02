

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Monotonicity is either increasing or decreasing
    # Start by assuming increasing
    is_increasing = True
    # Loop through all elements in list
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            # If a later element is less than previous element
            # Monotonicity has changed to decreasing
            is_increasing = False
    return is_increasing

