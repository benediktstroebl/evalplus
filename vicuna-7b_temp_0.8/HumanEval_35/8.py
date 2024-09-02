

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # binary search
    lo = 0
    hi = len(l) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if l[mid] == l[mid - 1]:
            lo = mid + 1
        elif l[mid] > l[mid - 1]:
            hi = mid - 1
        else:
            return l[mid]
    return l[lo]