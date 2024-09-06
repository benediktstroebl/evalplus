

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    direction = None
    for i in range(len(l) - 1):
        current_diff = l[i+1] - l[i]
        if direction is None:
            direction = current_diff
        elif current_diff != 0 and current_diff / direction < 0:
            return False
    return True
