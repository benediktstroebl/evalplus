

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # 1st we need to check the sign of the diffs
    diff = [l[i+1] - l[i] for i in range(len(l)-1)]
    signs = set(map(lambda x: x>0, diff))
    if len(signs) != 1:
        return False
    # second we need to check that sign of each diff is the same as the first diff
    return all(diff[0] * (l[i+1] - l[i]) > 0 for i in range(len(l)-1))
