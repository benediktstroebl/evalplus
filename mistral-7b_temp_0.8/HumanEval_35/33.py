

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 1:
        return l[0]
    else:
        max_ele = max_element(l[:-1])
        if max_ele >= l[-1]:
            return max_ele
        else:
            return l[-1]

