

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Given 2 elements:
    # if first element is smaller than the second, return True, because elements are monotonically decreasing
    # if first element is bigger than the second, return False, because elements are monotonically increasing
    # if both elements are equal, return True
    if len(l) == 1:
        return True
    if l[0] > l[1]:
        return False
    elif l[0] < l[1]:
        return True

    # Test 3 elements:
    # if first element is smaller than the second, but the second is smaller than the third, return True, because elements are monotonically decreasing
    # if first element is bigger than the second, but the second is bigger than the third, return True, because elements are monotonically increasing
    # if first element is smaller than the second, and the second is smaller than the third, return False, because elements are neither increasing nor decreasing
    if len(l) == 2:
        return monotonic(l)

    if l[0] > l[1] and l[1] > l[2
