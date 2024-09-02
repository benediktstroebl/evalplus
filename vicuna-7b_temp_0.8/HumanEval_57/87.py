

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # if list is empty return False
    if not l:
        return False

    # check if last two elements of list are the same
    last_two = l[-2:]+l[-1]
    if len(last_two) > 1:
        # if they are the same, list is not monotonically increasing or decreasing
        if last_two[0] <= last_two[1]:
            return False
    else:
        # if last two elements are not the same, list is not monotonically increasing or decreasing
        if l[-1] < l[-2]:
            return False

    # check if any other element is less than the element before it
    # (this is a sufficient condition for the list to be monotonically increasing)
    for i in range(len-1):
        if l[i] < l[i+1]:
            return False

    return True