

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
    for index in range(len(l)-1):
        if l[index] > l[index + 1]:
            increasing = False
        if l[index] < l[index + 1]:
            decreasing = False
    return increasing or decreasing

