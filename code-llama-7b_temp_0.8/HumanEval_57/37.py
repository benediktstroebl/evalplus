

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    decreasing = False
    for i in range(1, len(l)):
        if l[i - 1] == l[i]:
            continue
        elif (l[i - 1] < l[i] and not decreasing) or (l[i - 1] > l[i] and decreasing):
            return False
        elif l[i - 1] < l[i]:
            decreasing = False
        else:
            decreasing = True
    return True

