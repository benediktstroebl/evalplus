

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # make a copy so it's not changed while iterating over it
    l2 = l[:]
    # if all elements are the same, the list is monotonic
    if all(x == l2[0] for x in l2[1:]):
        return True
    # if the list is empty, it's monotonic
    if len(l2) == 0:
        return True
    # if the list is of length 1, it's monotonic
    if len(l2) == 1:
        return True
    # find the largest value in the list
    max_val = max(l2)
    # find the smallest value in the list
    min_val = min(l2)
    # find where the difference between max and min is
    min_max_diff = min_val - max_val
    # if the difference is greater than 0, elements are increasing
    if min_max_diff > 0:
        # if the difference is greater than all other differences, return True
        if min_max_diff < l2[0] - l2[-1]:
            return True
        # return False as soon as the difference is no longer positive
        return False
    # if the difference is less than 0, elements are decreasing
    elif min_max_diff < 0:
        # if the difference is less than all other differences, return True
        if min_max_diff < l2[0] - l2[-1]:
            return True
        # return False as soon as the difference is no longer positive
        return False
    # if the difference is 0, elements are either increasing or decreasing
    else:
        # return True or False as soon as a difference is no longer positive
        return False


assert(monotonic([1, 2, 4, 20]) == True)
assert(monotonic([1, 20, 4, 10]) == False)
assert(monotonic([4, 1, 0, -10]) == True)
