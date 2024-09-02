

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Using an accumulator with the None value
    last_value = None

    for v in l:
        if last_value and last_value < v:
            return False
        if last_value and last_value > v:
            return False

        last_value = v

    return True

