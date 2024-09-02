

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # first = l[0]
    # last = l[-1]
    #
    # if first > last:
    #     diff = list(map(lambda x: x - 1, l))
    #     return all(x <= y for x, y in zip(l, diff))
    # else:
    #     diff = list(map(lambda x: x + 1, l))
    #     return all(x >= y for x, y in zip(l, diff))

    diff = l[1:] - l[:-1]
    return diff.max() >= 0 or diff.min() <= 0

