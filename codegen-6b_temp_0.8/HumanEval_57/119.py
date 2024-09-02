

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # monotonic_decreasing = False
    # monotonic_increasing = False
    # for i in range(1, len(l)):
    #     if l[i] >= l[i - 1]:
    #         monotonic_increasing = True
    #         break
    # for i in range(1, len(l)):
    #     if l[i] <= l[i - 1]:
    #         monotonic_decreasing = True
    #         break
    # if monotonic_decreasing and monotonic_increasing:
    #     return True
    # else:
    #     return False
    return all(l[i] >= l[i - 1] for i in range(1, len(l))) or \
           all(l[i] <= l[i - 1] for i in range(1, len(l)))

