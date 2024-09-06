

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    is_inc = None
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            if is_inc is None:
                is_inc = False
            elif not is_inc:
                return False
        elif l[i-1] < l[i]:
            if is_inc is None:
                is_inc = True
            elif is_inc:
                return False
    return True
