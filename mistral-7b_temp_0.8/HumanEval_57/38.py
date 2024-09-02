

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    n = len(l)
    if n == 1:
        return True
    if n == 2:
        return l[1] > l[0] or l[1] < l[0]

    mid = n // 2
    mid_left = l[mid - 1]
    mid_right = l[mid]

    if mid == 1:
        return l[0] > l[1] or l[0] < l[1]

    if n % 2 == 1:
        return l[mid] < mid_right or l[mid] > mid_left
    else:
        return l[mid] > mid_right or l[mid] < mid_left

