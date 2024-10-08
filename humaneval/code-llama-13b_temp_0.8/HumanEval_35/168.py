

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # mx = max(l)  # M1
    mx = l[0]  # M2
    for x in l:
        if x > mx:
            mx = x
    return mx

