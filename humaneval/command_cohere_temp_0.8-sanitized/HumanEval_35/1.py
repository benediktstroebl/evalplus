def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list.

    Returns:
        int or float: The maximum element in the list.
    """
    # initialize max_element to the first element in the list
    max_element = l[0]
    # iterate through the list comparing each element
    # with the current max_element
    for x in l:
        if x > max_element:
            max_element = x
    return max_element