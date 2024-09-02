

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
        if mid - 1 in l:
            if l[mid] < l[left]:
                right = mid
            else:
                left = mid + 1
        else:
            left = right + 1
    return left <= max(l) <= right
