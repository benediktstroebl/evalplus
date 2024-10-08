

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # return l.sort(reverse=True)[0]
    max_elem = l[0]
    for element in l:
        if max_elem < element:
            max_elem = element
    return max_elem
