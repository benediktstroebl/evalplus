

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # if list has less than 2 elements it is monotonic
    if len(l) < 2:
        return True
    # if first and last elements are the same then list is monotonic
    if l[0] == l[-1]:
        return True

    if l[0] > l[-1]:
        for i in range(1, len(l)):
            if l[i-1] < l[i]:
                return False
    elif l[0] < l[-1]:
        for i in range(1, len(l)):
            if l[i-1] > l[i]:
                return False
    return True

