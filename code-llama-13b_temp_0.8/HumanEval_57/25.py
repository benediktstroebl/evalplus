

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) == 1:
        return True
    elif len(l) == 2:
        return abs(l[0]-l[1]) == 1 or abs(l[0]-l[1]) == 0
    else:
        for i in range(len(l)-2):
            if abs(l[i]-l[i+1]) != 1 and abs(l[i+1]-l[i+2]) != 1:
                return False
    return True

