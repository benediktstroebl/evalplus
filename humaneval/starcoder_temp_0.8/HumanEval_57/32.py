

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True
    dir = None
    for i in range(1, len(l)):
        if l[i - 1] < l[i]:
            if dir!= "increasing":
                dir = "increasing"
            continue
        elif l[i - 1] > l[i]:
            if dir!= "decreasing":
                dir = "decreasing"
            continue
        else:
            return True
    return False
