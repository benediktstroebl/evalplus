

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    left, right = 0, len(l)
    while left < right:
        mid = (left + right) // 2
        if l[mid] <= l[right]:
            left = mid + 1
        else:
            right = mid
    return left == right
