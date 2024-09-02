

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    assert len(l) > 1, "Must have more than one element"
    # The list is monotonically increasing if the list elements are all greater
    # than the next element in the list.
    is_increasing = all(l[i] > l[i+1] for i in range(len(l)-1))
    # The list is monotonically decreasing if the list elements are all less
    # than the next element in the list.
    is_decreasing = all(l[i] < l[i+1] for i in range(len(l)-1))
    return is_increasing or is_decreasing

