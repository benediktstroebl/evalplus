

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # if not l or len(l) == 1:
    #     return True
    # if l[0] >= l[1]:
    #     if all(x <= y for x, y in zip(l, l[1:])):
    #         return True
    # else:
    #     if all(x >= y for x, y in zip(l, l[1:])):
    #         return True
    # return False
    n = len(l)
    if n < 2:
        return True
    step = l[1] - l[0]
    if step == 0:
        return monotonic(l[1:])
    if step > 0:
        return monotonic([l[0]] + [y for x, y in zip(l, l[1:]) if x <= y])
    return monotonic([l[0]] + [y for x, y in zip(l, l[1:]) if x >= y])

