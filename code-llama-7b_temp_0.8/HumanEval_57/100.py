

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # if len(l) < 2:
    #     return False

    direction = None

    for i in range(len(l) - 1):
        if direction is None:
            direction = l[i + 1] - l[i]
            # print('direction: {}'.format(direction))
            continue

        if direction == 0:
            continue

        if (l[i + 1] - l[i] > 0) and direction < 0:
            return False

        if (l[i + 1] - l[i] < 0) and direction > 0:
            return False

    return True

