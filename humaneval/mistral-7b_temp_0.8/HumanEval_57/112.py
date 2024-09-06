

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    print('List:', l)
    for i in range(1, len(l)):
        print('Test:', l[i-1], ' and ', l[i])
        if l[i-1] > l[i]:
            return False
        elif l[i-1] < l[i]:
            return True
    return True
