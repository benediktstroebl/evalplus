

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    # for i in range(1, len(l)):
    #     if l[i] < l[i - 1]:
    #         return False
    # return True

    direction = 0
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            if direction != -1:
                return False
            else:
                direction = -1
        elif l[i] > l[i - 1]:
            if direction != 1:
                direction = 1
            else:
                return False
    return True
