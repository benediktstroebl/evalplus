

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    inc = 1
    for i in range(1, len(l)):
        if l[i - 1] < l[i]:
            inc = 1
        elif l[i - 1] > l[i]:
            inc = -1
        else:
            continue
        if i > 1 and inc != 0 and inc * (-1) != inc * (l[i-1] > l[i-2]):
            return False
    return True
