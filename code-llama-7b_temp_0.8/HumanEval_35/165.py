

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Check that there are some items in the list
    if len(l) == 0:
        return None

    # Set the first element as the maximum
    max_el = l[0]

    # Iterate through the list
    for el in l:
        # Check if the current element is larger than the previous maximum
        if el > max_el:
            max_el = el

    return max_el

