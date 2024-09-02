

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    left, right = 0, max(len(l) - 1)
    while left < right:
        mid = (left + right) // 2
        if l[left] <= l[mid] and l[mid] <= l[right]:
            return False
        elif l[left] >= l[mid] and l[mid] >= l[right]:
            return True
        left += 1
    return True
