

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if not l:
        return True

    op = None

    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            if op is None:
                op = 1
            elif op == -1:
                return False
        elif l[i] < l[i-1]:
            if op is None:
                op = -1
            elif op == 1:
                return False

    return True


