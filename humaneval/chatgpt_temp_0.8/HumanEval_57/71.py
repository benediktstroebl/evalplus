def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = decreasing = True  # Assume list is monotonically increasing and decreasing
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            increasing = False
        elif l[i] < l[i+1]:
            decreasing = False
        # If element is equal to the next element, then do not change any of the flags
    return increasing or decreasing
