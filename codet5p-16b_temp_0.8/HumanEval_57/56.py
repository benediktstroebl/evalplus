

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if len(l) <= 2:
        return True

    if l[0] > l[1]:
        inc = True
    elif l[0] < l[1]:
        inc = False
    else:
        inc = None

    for i in range(1, len(l) - 1):
        if inc is None:
            if l[i] > l[i+1]:
                inc = True
            elif l[i] < l[i+1]:
                inc = False
        elif inc == True:
            if l[i] >= l[i+1]:
                return False
        elif inc == False:
            if l[i] <= l[i+1]:
                return False

    return True


