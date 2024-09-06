

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # 1 
    # only have 2 options of increasing or decreasing
    # 2
    # check if the first item is increasing
    # 3
    # and check for every item after that
    # if it is in the same direction
    # if not, return false
    if len(l) == 1:
        return True
    if l[0] >= l[1]:
        for i in range(1, len(l)):
            if l[i] < l[i-1]:
                return False
        return True
    else:
        for i in range(1, len(l)):
            if l[i] >= l[i-1]:
                return False
        return True


