

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # In the case where there are no elements in the list, return None.
    if len(l) == 0:
        return None
    # In the case where there are more than 1 element in the list,
    # Return the max value in the list.
    max_value = l[0]
    for i in range(1, len(l)):
        if l[i] > max_value:
            max_value = l[i]
    return max_value
