

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    start = 0
    end = len(l) - 1
    while start < end:
        middle = (start + end) // 2
        if l[middle] > l[start]:
            end = middle - 1
        else:
            start = middle + 1
    return True