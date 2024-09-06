

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    left, right = 1, 1
    while left <= right:
        mid = (left + right) // 2
        if mid in l:
            if l[mid] > l[left]:
                return True
            elif l[mid] < l[right]:
                return False
        else:
            return False
    return False
