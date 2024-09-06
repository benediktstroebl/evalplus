

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    left, right = 1, max(l)
    while left < right:
        mid = (left + right) // 2
        if mid == 1 and l[left] < l[mid]:
            left = mid + 1
        elif mid == 2 and l[left] <= l[mid] and l[left] < l[right]:
            right = mid
        else:
            return False
    return True
