

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # Choose an element to start with. We can do this because the list is
    # non-empty.
    max_elem = l[0]

    # Examine each element in the list one by one and see if it is larger than
    # the current maximum element. If it is, change it.
    for elem in l[1:]:
        if elem > max_elem:
            max_elem = elem

    return max_elem

