

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    left, right = 0, len(l) - 1
    while left < right:
        mid = (left + right) // 2
        if l[mid] > l[left]:
            left = mid + 1
        elif l[mid] < l[right]:
            right = mid - 1
        else:
            return True
    return False