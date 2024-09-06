

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # find out if list is monotonically increasing or decreasing
    direction = None
    for i in range(len(l) - 1):
        diff = l[i + 1] - l[i]
        if direction is None:
            if diff == 0:
                continue
            elif diff > 0:
                direction = 'ascending'
            else:
                direction = 'descending'
        if direction == 'ascending' and diff <= 0:
            return False
        if direction == 'descending' and diff >= 0:
            return False
    return True

