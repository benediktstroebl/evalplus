

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    max_elem = l[0]
    for i in range(len(l)):
        if max_elem < l[i]:
            max_elem = l[i]
    return max_elem

