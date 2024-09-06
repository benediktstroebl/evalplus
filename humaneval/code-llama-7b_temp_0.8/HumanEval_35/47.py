

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # empty list?
    if not l:
        return None

    # start with first element as max
    max_elem = l[0]

    # loop through the list
    for elem in l[1:]:
        # if current element is greater than max, change max
        if elem > max_elem:
            max_elem = elem

    # return max element
    return max_elem

