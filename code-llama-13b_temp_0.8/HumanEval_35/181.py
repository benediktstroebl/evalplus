

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_so_far = l[0]
    for e in l:
        if e > max_so_far:
            max_so_far = e
    return max_so_far

