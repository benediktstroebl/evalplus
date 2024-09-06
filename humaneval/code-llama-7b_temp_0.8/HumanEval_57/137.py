

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    is_increasing = True
    is_decreasing = True
    for i in range(1, len(l)):
        if l[i - 1] > l[i]:
            is_increasing = False
        if l[i - 1] < l[i]:
            is_decreasing = False
    return is_increasing or is_decreasing

