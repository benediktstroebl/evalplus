

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # if the list is empty, return True
    if len(l) == 0:
        return True

    # if the list has only one element, return True
    elif len(l) == 1:
        return True

    # if the first element is less than the second element, return False
    elif l[0] > l[1]:
        return False

    # if the first element is greater than or equal to the second element, check if the following elements are increasing or decreasing
    else:
        for i in range(2, len(l)):
            if l[i] < l[i-1]:
                return False
        return True

