

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    def is_monotonic(l: list):
        """Return True is list elements are monotonically increasing or decreasing.

        >>> is_monotonic([1, 2, 4, 20])
        True
        >>> is_monotonic([1, 20, 4, 10])
        False
        >>> is_monotonic([4, 1, 0, -10])
        True
        """
        if len(l) < 2:
            return True
        prev = l[0]
        for i in range(1, len(l)):
            curr = l[i]
            if prev > curr:
                return False
            prev = curr
        return True
    return is_monotonic(l)

