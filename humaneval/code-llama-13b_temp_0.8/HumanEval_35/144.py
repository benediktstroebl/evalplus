

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # We initialize the maximum to be the first element.
    max_element = l[0]
    # We loop over the list, and update the maximum value.
    for element in l:
        if element > max_element:
            max_element = element

    # When we reach here, the max_element variable contains the maximum value.
    return max_element

