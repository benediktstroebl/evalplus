

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # create a dictionary to store the indices of the sorted elements
    indices = {i: i for i in range(len(l))}
    sorted_indices = sorted(indices.items())
    for start, end in sorted_indices:
        # check that the interval is sorted and contains only one element
        assert len(set(indices[start:end]).intersection(indices[start:end+1])) == 1
    return True