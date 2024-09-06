

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = False
    decreasing = False
    for n in range(len(l) - 1):
        if l[n] < l[n + 1]:
            increasing = True
        elif l[n] > l[n + 1]:
            decreasing = True
        if increasing and decreasing:
            return False
    return True
