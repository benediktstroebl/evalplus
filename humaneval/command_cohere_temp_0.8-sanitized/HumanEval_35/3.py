def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list of elements.

    Returns:
        int or float: The maximum element in the list.
    """
    if not l:
        return None  # Return None if the list is empty
    max_el = l[0]
    for num in l:
        if num > max_el:
            max_el = num
    return max_el