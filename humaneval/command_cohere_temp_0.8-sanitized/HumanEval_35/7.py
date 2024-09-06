def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list.

    Returns:
        int or float: The maximum element in the list.
    """
    if not l:
        return None
    max_el = max(l)
    return max_el