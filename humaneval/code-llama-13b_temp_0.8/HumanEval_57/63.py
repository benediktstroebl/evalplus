

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    inc = 0
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            inc = 1
        elif l[i] < l[i-1]:
            inc = -1
        if inc != 0 and inc != (l[i] - l[i-1]):
            return False
    return True

