

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    min_val = min(l)
    max_val = max(l)
    for i in range(1, len(l)):
        if l[i] <= min_val:
            return False
        elif l[i] >= max_val:
            return False
        elif l[i-1] > l[i]:
            return False
    return True