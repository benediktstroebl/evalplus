

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # if l is empty return None
    if not l:
        return None
    # set first element as the max
    m = l[0]
    # check if element at current index is greater than current max
    for e in l:
        if e > m:
            m = e
    # return max
    return m

