

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # important to return False if the list has only one element
    if len(l) <= 1:
        return False
    # as long as there is a monotonic relationship, keep going
    else:
        # should be the value of the first element
        prev = l[0]
        # loop through the rest of the list
        for element in l[1:]:
            # if the current element is less than the previous, we are decreasing
            if element < prev:
                # decreasing relationship must be true for all the rest of the list
                # in order to be monotonic
                if element >= prev:
                    return False
            # if the current element is greater than the previous, we are increasing
            elif element > prev:
                # increasing relationship must be true for all the rest of the list
                # in order to be monotonic
                if element <= prev:
                    return False
            else:
                return False
            prev = element
    return True


