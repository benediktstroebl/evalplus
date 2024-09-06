

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # ensure the list is not empty
    if not l:
        return False

    # If there is only one element, it is monotonic
    if len(l) == 1:
        return True

    # if the list is decreasing, check that each value is larger than the
    # next (both directions)
    if l[0] > l[1]:
        # check if the list is monotonically decreasing
        return all(l[i] > l[i+1] for i in range(len(l)-1))

    # if the list is increasing, check that each value is smaller than the
    # next (both directions)
    if l[0] < l[1]:
        # check if the list is monotonically increasing
        return all(l[i] < l[i+1] for i in range(len(l)-1))

    # if there are two or more elements but neither increasing nor decreasing,
    # the list is not monotonic
    return False

