

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    """
    monotonic increasing:
        [1, 2, 4, 20]
        [1, 10, 20, 30]

    monotonic decreasing:
        [10, 20, 30, 40]
        [0, -10, -20, -40]

    """

    decreasing = True
    increasing = True

    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            increasing = False
            break
        if l[i-1] < l[i]:
            decreasing = False
            break

    return increasing or decreasing


