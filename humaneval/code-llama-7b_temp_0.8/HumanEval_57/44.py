

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # can only be monotonic if it has a length of 1 or more
    if len(l) < 1:
        return False

    # if list is increasing, 
    if l[0] <= l[-1]:
        # check that every item is bigger than the last
        for i in range(len(l)):
            if l[i] < l[-1]:
                return False
    # if list is decreasing, 
    else:
        # check that every item is smaller than the last
        for i in range(len(l)):
            if l[i] > l[-1]:
                return False
    return True

