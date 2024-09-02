

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    print(l)
    if len(l) == 0:
        return None
    elif len(l) == 1:
        return l[0]
    else:
        mid = len(l) // 2
        if mid == 0:
            return l[0]
        elif mid == len(l):
            return l[-1]
        else:
            return max(max_element(l[:mid]), max_element(l[mid:]))

