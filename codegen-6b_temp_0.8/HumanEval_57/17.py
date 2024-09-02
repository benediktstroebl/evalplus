

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def is_non_decreasing(l):
        if len(l) < 2:
            return True
        elif l[0] > l[1]:
            return False

        return is_non_decreasing(l[1:])

    def is_non_increasing(l):
        if len(l) < 2:
            return True
        elif l[0] < l[1]:
            return False

        return is_non_increasing(l[1:])

    return is_non_decreasing(l) or is_non_increasing(l)

