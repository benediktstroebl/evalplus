

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        return None

    if len(l) == 1:
        return l[0]

    if len(l) == 2:
        if l[0] > l[1]:
            return l[0]
        else:
            return l[1]

    mid = len(l) // 2
    left = l[0: mid]
    right = l[mid:]

    l_max = max_element(left)
    r_max = max_element(right)

    if l_max is None:
        return r_max
    elif r_max is None:
        return l_max
    else:
        return l_max if l_max > r_max else r_max

