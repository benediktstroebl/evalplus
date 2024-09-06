

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # l_sign = 0 if l[1] == l[0] else (1 if l[1] > l[0] else -1)
    # for i in range(2, len(l)):
    #     if l[i] == l[i - 1]:
    #         continue
    #     elif (l[i] > l[i - 1]) != (l_sign > 0):
    #         return False
    # return True

    def _sign(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    if len(l) < 2:
        return True
    l_sign = _sign(l[1] - l[0])
    for i in range(2, len(l)):
        if l[i] == l[i - 1]:
            continue
        elif _sign(l[i] - l[i - 1]) != l_sign:
            return False
    return True

