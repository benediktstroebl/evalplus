

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # sign = None
    # for i in range(1, len(l)):
    #     if l[i] > l[i-1]:
    #         if sign is None:
    #             sign = 1
    #         elif sign != 1:
    #             return False
    #     elif l[i] < l[i-1]:
    #         if sign is None:
    #             sign = -1
    #         elif sign != -1:
    #             return False
    # return True
    return all(a >= b for a, b in zip(l, l[1:])) or all(a <= b for a, b in zip(l, l[1:]))

