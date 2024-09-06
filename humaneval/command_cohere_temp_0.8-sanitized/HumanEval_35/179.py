def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list of elements.

    Returns:
        int or float: The maximum element in the list.
    """
    # initialize maximum element
    max_el = float('-inf')

    # iterate through the list and update maximum element if necessary
    for x in l:
        if x > max_el:
            max_el = x

    return max_el